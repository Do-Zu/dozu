'use strict';
// Unit boundaries: real compiled methods, explicit query/provider doubles, no financial transaction.
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.resolve(__dirname,'../..'),dist=path.join(root,'apps/api/dist');
function load(relative,deps) {
    const filename=path.join(dist,relative),module={exports:{}};
    const wrapper=vm.runInNewContext(`(function(exports,require,module,__filename,__dirname){${fs.readFileSync(filename,'utf8')}\n})`);
    wrapper(module.exports,name=>{
        if(!Object.hasOwn(deps,name)) throw Error(`Unexpected dependency: ${relative}: ${name}`);
        return deps[name];
    },module,filename,path.dirname(filename));
    return module.exports;
}
class Unavailable extends Error {constructor(message){super(message);this.statusCode=503;}}
const errors={ServiceUnavailable:Unavailable,BadRequest:Error,DatabaseError:Error};
const guard=load('services/payment/paymentAvailability.service.js',{'@/core/error':errors});
let writes=0,where,lastLimit,reads=0;
const rows=[{transactionId:77,gateway:'payos',status:'success',amount:'100',userId:42}];
const forbidden=()=>{writes++;throw Error('A disabled payment touched mutable state');};
const query={from(){return this;},where(value){where=value;return this;},orderBy(){return this;},
    async limit(value){lastLimit=value;return rows;}};
const db={select(){reads++;return query;},insert:forbidden,update:forbidden,transaction:forbidden};
const model=new Proxy({}, {get:(_target,key)=>key});
const orm={eq:(column,value)=>({column,value}),and:(...clauses)=>clauses,desc:column=>column};
const logger={error(){},warn(){}};
const payment=load('services/payment/payment.service.js',{
    '@/libs/drizzleClient.lib':db,'@/models/payment/transaction.model':{transactionsModel:model},
    '@/core/error':errors,'@/utils/logger':logger,
    '@/services/payment/paymentAvailability.service':guard,'drizzle-orm':orm,
}).paymentService;
let response;
const success={ok:(_res,data)=>{response=data;}};
const controllers=load('controllers/payment/payment.controller.js',{
    '@/core/error':errors,'@/core/success':{SuccessResponse:success},
    '@/services/payment/payment.service':{paymentService:payment},'@/services/payment/paymentAvailability.service':guard,
    '@/utils/auth/authHelpers.utils':{getUserIdFromRequest:()=>42},
}).paymentController;
const neverAccess=new Proxy({}, {get:()=>forbidden});
const subscriptions=load('controllers/subscription/subscription.controller.js',{
    '@/core/error':errors,'@/core/success':{SuccessResponse:success},
    '@/services/payment/paymentAvailability.service':guard,
    '@/services/subscription/subscription.service':neverAccess,'@/utils/date':neverAccess,
    '@/dtos/subscription/subscription.dto':neverAccess,'@/utils/auth/authHelpers.utils':neverAccess,
    '@/utils/common':neverAccess,
});
const admin=load('services/admin/payment.service.js',{
    '@/services/payment/paymentAvailability.service':guard,'@/libs/drizzleClient.lib':db,'drizzle-orm':orm,
    '@/models/payment/transaction.model':{transactionsModel:model},'@/models/user.model':{usersTable:model},
}).adminPaymentService;
async function main() {
    const actions=[];
    for(const name of ['createLinkPaymentWithPayOS','handleWebhookPayOS','handleWebhookSepay',
        'connectPaymentSSE','updateTransactionStatus']) {
        await assert.rejects(controllers[name]({body:{status:'PAID',success:true,planId:2},query:{status:'PAID'}},{}),e=>e.statusCode===503);
        actions.push(name);
    }
    await assert.rejects(payment.createPaymentLinkWithPayOS({planId:2,userId:42,amount:100,timeZone:'Asia/Bangkok'}),e=>e.statusCode===503);
    await assert.rejects(payment.updateTransactionStatus({userId:42,status:'success'}),e=>e.statusCode===503);
    const subscription=new subscriptions.SubscriptionController();
    await assert.rejects(subscription.createSubscription({},{}),e=>e.statusCode===503);
    await assert.rejects(subscription.upgradeSubscription({},{}),e=>e.statusCode===503);
    await assert.rejects(admin.updateTransactionStatus(77,{status:'success'}),e=>e.statusCode===503);
    await assert.rejects(admin.refundTransaction({transactionId:77,amount:100}),e=>e.statusCode===503);
    assert.equal(reads,0);assert.equal(writes,0);assert.equal(response,undefined);
    const history=await payment.getUserTransactionHistory(42,2);
    assert.equal(history,rows);assert.equal(lastLimit,2);assert.equal(where.column,'userId');assert.equal(where.value,42);
    await controllers.getTransactionHistory({query:{limit:'2'}},{});
    assert.equal(response,rows);assert.equal(lastLimit,2);assert.equal(writes,0);
    assert.equal(history[0].gateway,'payos');assert.equal(history[0].status,'success');
    assert.equal(fs.existsSync(path.join(root,'apps/api/node_modules/@payos/node')),false);
    const page=fs.readFileSync(path.join(root,'apps/web/src/app/[locale]/payment/page.tsx'),'utf8');
    for(const forbiddenToken of ['usePayment','useSearchParams','initializePayment','updateSubscription']) {
        assert.equal(page.includes(forbiddenToken),false,forbiddenToken);
    }
    const report={passed:true,disabledControllerActions:actions,disabledDirectServices:true,
        disabledPaidSubscriptionMutations:true,disabledAdminRefundAndStatusMutation:true,
        disabledActionsReadOrWriteCount:0,historicalReadsPreserveGatewayStatusAndUserFilter:true,
        payosSdkDirectLinkAbsent:true,checkoutPageHasNoPaymentOrCallbackEffects:true,
        boundary:'Compiled services/controllers with explicit query/provider doubles; no actual DB, payment, refund, HTTP, signed JWT or browser interaction.'};
    fs.writeFileSync(path.join(__dirname,'contract-check.json'),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify(report,null,2));
}
main().catch(error=>{console.error(error);process.exitCode=1;});
