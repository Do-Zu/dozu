'use strict';
// Real isolated PostgreSQL/BullMQ evaluation. No app modules, mocked Redis or providers.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const {createRequire}=require('node:module');
const load=createRequire(path.join(__dirname,'.runs/queue-evaluation/package.json'));
const {Pool}=load('pg');
const {withBackend,createPostgresBackend,runMigrations}=load('bullmq');
const {Queue,Worker,QueueEvents}=withBackend(createPostgresBackend);
const phase=process.argv[2];
const schema='dozu_queue_probe';
const cfg={host:'127.0.0.1',port:Number(process.env.DOZU_PROBE_PORT),user:'dozu_probe',password:process.env.DOZU_PROBE_PASSWORD,database:'postgres',max:2};
const opts={connection:{...cfg,schema}};
const checks=[];
const objects=[];
const pool=new Pool(cfg);
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function check(name, action){await action();checks.push(name);}
async function main(){
  const client=await pool.connect();
  try{await runMigrations(client,schema);await runMigrations(client,schema);}finally{client.release();}
  checks.push('explicit PostgreSQL schema migration is repeatable');
  const queue=new Queue('generation_probe',opts);objects.push(queue);
  if(phase==='before'){
    await check('queue accepts pending job without worker',async()=>{
      const job=await queue.add('persisted',{kind:'persisted',value:7},{jobId:'survive-restart',removeOnComplete:false});
      assert.equal(await job.getState(),'waiting');
    });
    await pool.query('CREATE SCHEMA IF NOT EXISTS dozu_state_probe');
    await pool.query('CREATE TABLE IF NOT EXISTS dozu_state_probe.counters(key text PRIMARY KEY, value bigint NOT NULL)');
    await check('concurrent durable counter increments preserve every update',async()=>{
      await Promise.all(Array.from({length:40},()=>pool.query("INSERT INTO dozu_state_probe.counters VALUES ('usage',1) ON CONFLICT(key) DO UPDATE SET value=dozu_state_probe.counters.value+1")));
      assert.equal((await pool.query("SELECT value FROM dozu_state_probe.counters WHERE key='usage'")).rows[0].value,'40');
    });
    await pool.query('CREATE TABLE dozu_state_probe.results(key text PRIMARY KEY, payload jsonb NOT NULL, expires_at timestamptz)');
    await pool.query("INSERT INTO dozu_state_probe.results VALUES ('result', $1::jsonb, now()+interval '1 hour'), ('expired', '{}'::jsonb, now()-interval '1 second')",[JSON.stringify({text:'genuine probe result tiếng Việt'})]);
    await check('expired cache entries are excluded by authoritative timestamp',async()=>{
      const r=await pool.query('SELECT key FROM dozu_state_probe.results WHERE expires_at > now()');
      assert.deepEqual(r.rows.map(x=>x.key),['result']);
    });
  }else{
    await check('queued job and durable state survive actual PostgreSQL restart',async()=>{
      assert.equal(await (await queue.getJob('survive-restart')).getState(),'waiting');
      assert.equal((await pool.query("SELECT value FROM dozu_state_probe.counters WHERE key='usage'")).rows[0].value,'40');
      assert.equal((await pool.query("SELECT payload FROM dozu_state_probe.results WHERE key='result'")).rows[0].payload.text,'genuine probe result tiếng Việt');
    });
    const events=new QueueEvents('generation_probe',opts); objects.push(events);
    const observed=[];const failures=[];
    events.on('completed',x=>observed.push({type:'completed',id:x.jobId}));
    events.on('progress',x=>observed.push({type:'progress',id:x.jobId}));
    events.on('error',e=>failures.push(e.message));
    await events.waitUntilReady();
    const processed=[];
    const worker=new Worker('generation_probe',async job=>{
      processed.push({id:job.id,kind:job.data.kind,attemptsMade:job.attemptsMade});
      if(job.data.kind==='permanent-failure')throw new Error('intentional permanent fixture');
      if(job.data.kind==='retry'&&job.attemptsMade<1)throw new Error('intentional retry fixture');
      await job.updateProgress(50);
      return {value:job.data.value*2,kind:job.data.kind};
    },{...opts,concurrency:2});objects.push(worker);
    worker.on('error',e=>failures.push(e.message));
    await worker.waitUntilReady();
    const persisted=await queue.getJob('survive-restart');
    await check('worker consumes persisted job and returns actual result',async()=>{
      assert.deepEqual(await persisted.waitUntilFinished(events,20000),{value:14,kind:'persisted'});
    });
    const retry=await queue.add('retry',{kind:'retry',value:3},{jobId:'retry-id',attempts:3,backoff:{type:'exponential',delay:150}});
    await check('failed job retries with backoff and completes',async()=>{
      assert.deepEqual(await retry.waitUntilFinished(events,20000),{value:6,kind:'retry'});
      assert.equal(processed.filter(x=>x.id==='retry-id').length,2);
    });
    const start=Date.now();
    const delayed=await queue.add('delayed',{kind:'delayed',value:4},{jobId:'delayed-id',delay:500});
    await check('delayed job is not consumed before its delay',async()=>{
      assert.deepEqual(await delayed.waitUntilFinished(events,20000),{value:8,kind:'delayed'});
      assert(Date.now()-start>=450);
    });
    await check('duplicate job ID does not execute again',async()=>{
      await queue.add('duplicate',{kind:'persisted',value:99},{jobId:'survive-restart'});
      await sleep(200);
      assert.equal(processed.filter(x=>x.id==='survive-restart').length,1);
      assert.equal((await queue.getJob('survive-restart')).returnvalue.value,14);
    });
    const failed=await queue.add('failure',{kind:'permanent-failure',value:1},{jobId:'failed-id',attempts:2,backoff:{type:'fixed',delay:100}});
    await check('exhausted attempts retain failed state and reason',async()=>{
      await assert.rejects(failed.waitUntilFinished(events,20000),/intentional permanent fixture/);
      const stored=await queue.getJob('failed-id');
      assert.equal(await stored.getState(),'failed');
      assert.equal(stored.attemptsMade,2);
    });
    await check('QueueEvents reports real completion and progress',async()=>{
      for(let i=0;i<40&&!observed.some(x=>x.type==='progress');i++)await sleep(50);
      assert(observed.some(x=>x.type==='completed'&&x.id==='retry-id'));
      assert(observed.some(x=>x.type==='progress'));
      assert.deepEqual(failures,[]);
    });
    const tables=(await pool.query('SELECT tablename FROM pg_tables WHERE schemaname=$1 ORDER BY tablename',[schema])).rows.map(x=>x.tablename);
    fs.writeFileSync(path.join(__dirname,'postgres-observed.json'),JSON.stringify({bullmq:'6.7.6',pg:'8.14.1',processed,events:observed,tables},null,2)+'\n');
  }
  return {phase,checks,passed:checks.length,redisUsed:false,scope:'Real isolated Windows PostgreSQL and queue/counter/resource-contract proof; application adapters/provider/UI/native clean-machine acceptance not tested'};
}
(async()=>{
  let result;
  try{result=await main();}
  catch(e){result={phase,checks,error:e.message,stack:e.stack};process.exitCode=1;}
  finally{
    for(const obj of objects.reverse())try{await obj.close();}catch(e){process.exitCode=1;}
    await pool.end();
  }
  fs.writeFileSync(path.join(__dirname,'postgres-'+phase+'.json'),JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify(result));
})();
