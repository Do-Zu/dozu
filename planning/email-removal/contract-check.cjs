'use strict';
// Execute actual compiled services with explicit repository/provider doubles.
// These are unit boundary checks, not a real database/login/notification proof.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '../..');
const dist = path.join(root, 'apps/api/dist');
const checks = [];
function load(relative, dependencies, env = {}) {
    const filename = path.join(dist, relative);
    const code = fs.readFileSync(filename, 'utf8');
    const module = { exports: {} };
    const wrapper = vm.runInNewContext(`(function(exports,require,module,__filename,__dirname,process,Buffer){${code}\n})`);
    wrapper(module.exports, (name) => {
        if (!Object.hasOwn(dependencies, name)) throw new Error(`Unexpected dependency: ${relative}: ${name}`);
        return dependencies[name];
    }, module, filename, path.dirname(filename), { env, stdout: {write() {}}, stderr: {write() {}} }, Buffer);
    return module.exports;
}
class Unavailable extends Error { constructor(message) { super(message); this.statusCode = 503; } }
const errors = { ServiceUnavailable: Unavailable, DatabaseError: Error, InternalServerError: Error,
    BadRequest: Error, NotFoundError: Error };
const email = load('libs/email.lib.js', { '@/core/error': errors });
const logger = {info() {},warn() {},error() {}};
const hashes = load('utils/auth/hash.utils.js', {crypto:require('node:crypto'),util:require('node:util')});
let writes = 0;
const forbiddenRepository = new Proxy({}, {get: () => () => { writes++; throw Error('Unexpected repository access'); }});
let user;
const repository = {
    selectOneUserByEmailOrUsername: async () => null,
    insertUser: async (username, passwordHash, emailAddress) => {
        writes++;
        user = {userId:1, username, passwordHash, email:emailAddress, isActive:true, isVerified:false};
        return user;
    },
    getUserRoleId: async () => 1,
    addRole: async () => {writes++;},
    getRoles: async () => [{roleId:1,name:'user'}],
    getUserRoles: async () => [{roleId:1}],
    updateLastLoginAt: async () => user,
    selectOneUserByUsername: async () => user,
    insertVerificationCode: async () => {throw Error('Verification code must not be created');},
};
const auth = load('services/auth.service.js', {
    '@/core/error':errors, '@/libs/googleOAuth2Client':{}, '@/libs/email.lib':email,
    './subscription/subscription.service':{createSubscriptionFreePlan:async () => {}},
    '@/repositories/profile/profile.repo':class {}, '@/repositories/auth.repo':repository,
    '@/repositories/auth/changePasswordRequest.repo':forbiddenRepository,
    '@/utils/auth/authHelpers.utils':{sanitizeUserObject: input => ({userId:input.userId,username:input.username})},
    '@/utils/auth/hash.utils':hashes,
    '@/utils/auth/jwt.utils':{signAccessJwtToken:()=> 'unit-access',signRefreshJwtToken:()=> 'unit-refresh'},
    '@/utils/logger':logger, jsonwebtoken:{},
    '@/utils/common':{isEmpty:input=> !input || Object.keys(input).length===0,safeDestructure:input=> input},
});
async function main() {
    const registered = await auth.registerUserService({username:'unit-user',password:'unit-password',
        email:'fixture@example.invalid',role:'user',timezone:'Asia/Bangkok'});
    assert.equal(registered.success,true); assert.equal(user.isVerified,false);
    assert.notEqual(user.passwordHash,'unit-password');
    assert.equal((await auth.loginService({username:'unit-user',password:'unit-password'})).success,true);
    assert.equal((await auth.loginService({username:'unit-user',password:'wrong-password'})).success,false);
    user.isActive=false;
    assert.equal((await auth.loginService({username:'unit-user',password:'unit-password'})).success,false);
    checks.push('signup and password login without email proof; wrong-password/inactive rejection');
    const before=writes;
    await assert.rejects(auth.sendChangePasswordLinkService({email:'fixture@example.invalid'}), e=> e.statusCode===503);
    assert.equal(writes,before);
    const invites=load('services/class-based-learning/classInvite.service.js', {
        '@/core/error':errors,'@/repositories/class-based-learning/classInvite.repo':forbiddenRepository,
        '@/services/user/userSearch.service':forbiddenRepository,
        '@/services/class-based-learning/classEnrollment.service':forbiddenRepository,
        '@/libs/email.lib':email,nanoid:{customAlphabet:()=>()=> 'unit-token'},
    }).default;
    await assert.rejects(invites.inviteByEmail(1,1,{emails:['fixture@example.invalid']}), e=> e.statusCode===503);
    assert.equal(writes,before);
    checks.push('email reset/invitation return 503 before repository reads or writes');
    let realtime=0;
    const notification=load('services/notification/notification.service.js', {
        '@/repositories/profile/profile.repo':class {},'@/utils/logger':logger,
        '@/libs/websocket/notification.websocket':{NotificationWebSocketService:{getInstance:()=>({sendToUser:async()=>{realtime++;return true;}})}},
        './notification.email.templates':{},
    }).NotificationService;
    assert.equal(await notification.sendEmail({to:'fixture@example.invalid',subject:'unit',html:'unit'}),false);
    notification.getUserNotificationContext=async()=>({userId:1,username:'unit-user',fullName:null,
        settings:{dailyReminders:true,pushNotifications:false,emailNotifications:true}});
    assert.equal(await notification.sendDailyReminder(1),true); assert.equal(realtime,1);
    assert.equal(notification.getUserNotifications(1).length,1);
    checks.push('email reports false; in-app reminder delivered without SMTP/frontend URL settings');
    let savedFeedback;
    const feedback=load('services/feedback/feedback.service.js', {
        '@/repositories/feedback/feedback.repo':{create:async input=>{savedFeedback=input;return {feedbackId:7};}},
        '@/services/feedback/feedback.evaluator':{evaluateFeedback:()=>({score:3,reasons:[],shouldSendEmail:true})},
    }).default;
    const feedbackResult=await feedback.submitFeedback({message:'Useful local feedback'});
    assert.equal(feedbackResult.success,true); assert.equal(feedbackResult.notified,false);
    assert.equal(savedFeedback.message,'Useful local feedback'); assert.equal(savedFeedback.shouldSendEmail,0);
    checks.push('feedback service persists the local record without claiming email notification');
    const configDeps={dotenv:{config:()=>{throw Error('Unexpected dotenv read');}},'node:path':path,fs:{existsSync:()=>false}};
    const config=env=>load('config/env.config.js',configDeps,env).config;
    assert.equal(config({}).backendBaseUrl,'http://localhost:3333');
    assert.equal(config({PORT:'4444',HOST:'0.0.0.0'}).backendBaseUrl,'http://localhost:4444');
    assert.equal(config({BACK_END_URL:'http://192.0.2.1:4444/'}).backendBaseUrl,'http://192.0.2.1:4444');
    assert.equal(config({BACKEND_BASE_URL:'https://example.invalid/api/',BACK_END_URL:'http://localhost:1'}).backendBaseUrl,'https://example.invalid/api');
    checks.push('backend local default, custom port, alias, canonical precedence and trailing slash');
    const report={checks,passed:true,boundary:'Compiled modules, explicit repository/provider doubles; real scrypt password hashing. No real database, mail, Redis, HTTP or JWT validation.'};
    fs.writeFileSync(path.join(__dirname,'contract-check.json'),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify(report,null,2));
}
main().catch(error=>{console.error(error);process.exitCode=1;});
