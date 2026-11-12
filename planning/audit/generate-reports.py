"""Render reviewable ledgers from source evidence; never mark source discovery as parity."""
from collections import Counter
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
def read(name): return json.loads((HERE / name).read_text(encoding='utf-8'))
def write(name, text): (HERE / name).write_text(text.rstrip()+'\n', encoding='utf-8')
def ref(source, line=1): return f'[{source}:{line}](<../../{source}#L{line}>)'
def cell(value): return str(value).replace('|', '\\|').replace('\n', ' ')
def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+['| '+' | '.join(cell(x) for x in row)+' |' for row in rows])

sources = read('source-inventory.json')
by_source = {s['source']:s for s in sources}
ui = read('ui-workflows.json')
api = read('backend-endpoints.json')
db = read('database-inventory.json')
config = read('configuration-inventory.json')

# Workflow descriptions were reviewed against page imports/render trees and their services.
special = {
 '': 'Choose redirect by account/onboarding state; show auth loading.',
 '/about': 'Read team/profile content.', '/blogs': 'Render Blog Page heading; placeholder, no blog CRUD.',
 '/welcome': 'Browse landing/FAQ, change language/theme and enter sign-in/onboarding.',
 '/auth/login': 'Password sign-in; real Google code redirect; preserve redirect destination and error/loading states.',
 '/auth/register': 'Create account, verification mail, Google sign-in, validation and login link.',
 '/auth/verifyEmail': 'Read email/code query, verify with backend, update session and navigate.',
 '/auth/forgotPassword': 'Request password-change email and show sent/error state.',
 '/auth/changePasswordEmailSent': 'Show delivery guidance and return navigation; not proof of email delivery.',
 '/auth/changePassword': 'Validate email/code query and submit new password.',
 '/auth/testBackEnd': 'Developer authentication/Redux test surface; preserve source, classify for release.',
 '/onboarding': 'Step through topic tags, duration and learning-method preferences; persist completion.',
 '/home': 'Guest preview or account library; packages/tree/topics CRUD, current learning, generate actions, learning-mode/admin redirects.',
 '/profile': 'Load/update personal information, avatar and notification/settings tabs.',
 '/setting/profile': 'Authenticated wrapper reusing profile page.',
 '/setting/schedule-setup': 'Configure study availability, frequency, methods and schedule preferences.',
 '/schedule': 'Calendar/list views, recommended slots and learning progress interactions.',
 '/progress': 'Progress dashboard with study totals and topic/method progress.',
 '/stats': 'LearningProgress component; verify supplied data and API use before claiming analytics.',
 '/generate': 'Choose text/file/URL/YouTube/media input, convert/transcribe, select model/content/difficulty, stream generation, preview/save study content.',
 '/payment': 'Select plan/payment method, genuine checkout/QR, cancel/return, realtime result and transaction status/history.',
 '/request-teacher': 'Read request status or submit teacher application.',
 '/request-teacher/reapply': 'Edit/resubmit teacher application after rejection.',
 '/topics/[topicId]': 'Topic workspace tabs for flashcards, quiz, mindmap, notes and media; generation/edit/learning and source-linked context.',
 '/topics/[topicId]/settings/anki': 'Select/create/update/delete Anki preset, edit parameters, assign to topic and reset defaults.',
 '/question/edit/[topicId]': 'Question editor: change questions/answers/options and persist topic quiz bank.',
 '/quiz/[topicId]/doing': 'Answer quiz, navigate questions, confirm submission and persist results.',
 '/quiz/[topicId]/history': 'List attempts and open result/history details.',
 '/quiz/[topicId]/history/[quizResultId]': 'Read historical attempt questions/answers and scoring details.',
 '/quiz/[topicId]/result/[quizResultId]': 'Display saved result and review answers.',
 '/quiz/local': 'Browser-storage quiz draft/answers plus streak update; shared DB authority requires explicit transfer contract.',
 '/feynman/[topicId]': 'Read mission/source, write explanation, request genuine AI questions/review, view history and save learning progress.',
 '/games/brain-chase': 'Flashcard-based game, pause/restart/settings and result/progress integration.',
 '/games/memory-match': 'Match flashcard pairs, timer/game state and completion behavior.',
 '/mindmap/[topicId]': 'Edit ReactFlow nodes/edges, flashcards/source sheet, generation, roadmap and export/import/save actions.',
 '/mindmap/view/[topicId]': 'View-only ReactFlow source/node sheets and export/download.',
 '/mindmap/add-flashcard': 'Select flashcards in table and attach to nodes; verify IDs/save integration.',
 '/mindmap/nodes/[id]': 'Mostly empty node page with parameter check; ReactFlow body commented out.',
 '/mindmap/nodes/[id]/flashcard': 'Temporary node flashcard list fetched through raw Axios; loading/empty/error states.',
 '/tests/class/comment': 'Empty developer route; not implemented comment UI.',
 '/class-based': 'Student class library, invitation/join and class navigation.',
 '/class-based/[id]': 'Student dashboard tabs: topics, feed, classwork/materials, assignments and quizzes.',
 '/teacher/home': 'Teacher class library and class management/navigation.',
 '/teacher/class-based/[id]': 'Teacher class dashboard, topics/feed/classwork tabs, create/edit/archive and access management.',
 '/teacher/class-based/[id]/students': 'List/search student enrollment, profile modal and enrollment management.',
 '/activities/join/[activityId]': 'Join quiz activity, show availability/status and start navigation.',
 '/admin': 'Account/role/activity dashboard cards and signup chart.',
 '/admin/stats': 'Fetch user statistics and render charts/loading state.',
 '/admin/users': 'Filter/page users; activate/deactivate, edit role and inspect OAuth associations.',
 '/admin/users/[id]/oauth': 'Read user linked authentication accounts and provider metadata.',
 '/admin/features': 'List/create/update/delete subscription features and limits.',
 '/admin/plans': 'List/create/edit/delete plans and navigate feature assignment.',
 '/admin/plans/[planId]/features': 'Assign/edit/remove plan feature access and limits.',
 '/admin/subscriptions': 'Subscription KPI/status/monthly charts with links to lists/plans/features.',
 '/admin/subscriptions/list': 'Filter/page subscription records and administer their states.',
 '/admin/revenue': 'Filter revenue and gateway/plan/trend analytics.',
 '/admin/payments': 'Filter/page payment ledger and export CSV.',
 '/admin/feedback': 'Filter/list feedback and update moderation/status/auto-ignore operations.',
 '/admin/teacher-requests': 'List teacher applications/statuses.',
 '/admin/teacher-requests/pending': 'Review pending applications and approve/reject.',
 '/admin/llm-providers': 'Create/edit/delete/filter providers, URLs and availability.',
 '/admin/llm-models': 'Create/edit/delete/filter provider models and availability.',
 '/admin/llm-api-keys': 'Create/edit/delete/filter provider keys and key status; sensitive DB-backed key handling.',
 '/admin/llm-api-key-models': 'Create/edit/delete key-model associations, priorities and quotas.',
}

def workflow(route):
    if route in special: return special[route]
    if '/assignments/' in route and route.endswith('/details'):
        return 'Read assignment/attachments/comments; '+('teacher reviews/grades submissions and edits/deletes assignment.' if route.startswith('/teacher') else 'student uploads/replaces/submits work and reads private feedback.')
    if route.endswith('/assignments'): return 'Create assignment, choose class/topics, rich text, attachments and scheduling; persist and return to class.'
    if '/assignments/' in route and route.endswith('/edit'): return 'Load/edit assignment, topics, rich text, attachments and scheduling.'
    if '/learning-material/' in route and route.endswith('/details'): return 'Read material content/attachments/comments; '+('teacher edit/delete actions.' if route.startswith('/teacher') else 'student read/comment actions.')
    if '/learning-material/' in route and route.endswith('/edit'): return 'Load/edit teaching material, content, attachments and associated topics.'
    if route.endswith('/learning-material'): return 'Create teaching material with topic/content/attachment selection.'
    if '/learning-material/' in route: return 'Read/download learning-material attachment from backend.'
    if '/class-quiz/' in route and route.endswith('/edit'): return 'Edit quiz draft/questions/settings and publish/schedule/close lifecycle.'
    if route.endswith('/class-quiz'): return 'List teacher quiz drafts/publications and navigate editing.'
    if '/class-quiz/' in route and route.endswith('/start'): return 'Student start timed attempt, autosave answers, receive quiz activity and confirm submit.'
    if '/class-quiz/' in route and route.endswith('/submit'): return 'Submit/review attempt and show result; preserve deadline/retry semantics.'
    if '/class-quiz/' in route and route.endswith('/history'): return 'List/review student attempt history with answers and timing.'
    if '/activities/' in route: return 'Teacher live quiz monitoring tabs, participation/answer events, refresh and XLSX results export.'
    if route.endswith('/generate'): return 'Teacher generation reuses full GeneratePage for class/topic content.'
    if '/mindmap/' in route: return 'Class topic ReactFlow mindmap, source and flashcard sheets, export; '+('teacher edit/save/generate actions.' if route.startswith('/teacher') else 'student read-only access.')
    if '/topics/' in route: return 'Class context wraps shared topic workspace and mindmap provider; preserve teacher/student permissions across tabs.'
    raise ValueError('Unreviewed route '+route)

def family(route):
    if route.startswith('/admin'): return ('Administration', 'admin intent; inspect explicit gate evidence', ['/api/admin'], [13,14,17,31,40])
    if route.startswith(('/class-based','/teacher','/activities')): return ('Classroom', 'teacher intent' if route.startswith('/teacher') else 'student/participant intent', ['/api/classes','/api/student/class-quiz','/api/teacher/class-quiz','/api/assignments','/api/quiz-class','/api/enrollments','/api/learning-material','/api/comments'], [17,19,27,30,43])
    if route.startswith('/auth'): return ('Accounts', 'guest/account/link callback; see gates', ['/api/auth'], [11,14,27,31,40,42])
    if route.startswith('/request-teacher'): return ('Teacher approval', 'authenticated account intent', ['/api/teacher-requests'], [14,17,40,43])
    if route.startswith(('/generate','/feynman')): return ('Generation and Feynman', 'authenticated; subscription/usage gating', ['/api/generate','/api/feynman','/api/event/generate','/api/upload','/api/convert','/api/youtube','/api/v1'], [8,18,19,21,30,32,40,44])
    if route.startswith('/payment'): return ('Billing', 'authenticated; provider callback', ['/api/payment','/api/subscription','/api/event/generate'], [19,27,30,31,41])
    if route.startswith(('/topics','/mindmap','/question','/quiz','/games')): return ('Study workspace', 'account/topic ownership intent; local-quiz also browser state', ['/api/topics','/api/flashcards','/api/mindmap','/api/questions','/api/quiz','/api/content','/api/tracking','/api/anki_settings','/api/backlog','/api/gamification','/api/v1/embedding'], [11,13,16,17,18,21,29,30,44])
    if route.startswith(('/profile','/setting','/schedule','/progress','/stats','/onboarding','/home')): return ('Personal learning', 'guest preview or authenticated personal data; see gates', ['/api/profile','/api/onboarding','/api/package','/api/topics','/api/schedule','/api/progress','/api/recommendation','/api/tracking','/api/notifications','/api/gamification'], [13,14,17,20,29,30,34,40])
    return ('Public and diagnostic', 'public/redirect/developer surface; no universal auth asserted', [], [13,17,32])

matrix=[]
for index,p in enumerate(ui['pages'],1):
    route=p['route'].replace('/[locale]','')
    fam,role,prefixes,issues=family(route)
    gates=[{'source':s,'line':c['line'],'call':c} for s in [p['source'],*p['layouts']] for c in by_source[s]['calls'] if c['kind']=='auth' or c['kind']=='jsx' and ('role' in c['callee'].lower() or 'permission' in c['callee'].lower())]
    endpoints=[{'method':e['method'],'path':e['path'],'source':e['source'],'line':e['line']} for e in api['endpoints'] if any(e['path']==x or e['path'].startswith(x+'/') for x in prefixes)]
    matrix.append({'id':f'UI-{index:03}', 'route':p['route'], 'source':p['source'], 'family':fam,'rolesAndWorkflows':role+'; '+workflow(route),'workflow':workflow(route),'gateEvidence':gates,'locales':['en','vi'],'layouts':p['layouts'],'directComponents':p['rendered'],'apiConsumerSources':p['apiConsumers'],'candidateBackendContracts':endpoints,'backendMappingConfidence':'family-level candidates, not an assertion that this page calls every endpoint','localDesktopImplication':'Retain existing page and layout in Next standalone; all first-party data/stream/socket/file traffic must share the same localhost Express and local PostgreSQL/files; user-scoped real external providers only.','uncertainty':'Source traced. Browser/Electron, role, locale, mutation/error/restart workflows have not passed runtime parity. Inspect gate evidence; route name alone is not authorization.','followUpIssues':[f'https://github.com/Do-Zu/dozu/issues/{n}' for n in issues],'runtimeParity':'UNVERIFIED'})

(HERE/'feature-parity.json').write_text(json.dumps({'auditDate':'2026-11-09','status':'Audit complete; desktop implementation/parity not complete','pages':matrix},indent=2),encoding='utf-8')
write('feature-parity.md', '# Complete UI feature-parity matrix\n\nAudit date: 2026-11-09. All 84 pages are represented individually. Every row retains en/vi, inherited layouts and existing interactions. **All runtime desktop parity is UNVERIFIED**. Counts and source tracing are inventory evidence, never a passing functional test. Role descriptions indicate intent; explicit gate sites are in JSON, not inferred authorization guarantees.\n\n[Detailed source/interaction ledger](ui-ledger.md) · [Machine-readable page/contract links](feature-parity.json) · [Backend endpoints](backend-endpoints.md) · [Findings and follow-up](findings.md)\n\n'+table(['ID / route','Existing workflow','Source / role intent','Follow-up'],[(m['id']+' `'+m['route']+'`',m['workflow'],ref(m['source'])+'; '+m['rolesAndWorkflows'].split(';')[0],', '.join('#'+u.rsplit('/',1)[-1] for u in m['followUpIssues'])) for m in matrix])+'\n\nEach workflow must later pass read/create/edit/delete where offered, keyboard/mouse/navigation, reload/back/deep-link, unauthorized/expired session, empty/error/loading state, en/vi and theme, disconnected/reconnected provider state, browser+Electron shared records, restart persistence and ownership. Payment/classroom tests additionally depend on #41/#43 decisions. Existing placeholders and broken links are retained audit findings, not newly implemented capabilities.')

parts=['# UI source and interaction ledger','', 'AST evidence covers all page/layout imports, TSX components, hooks/providers and navigation sites. Import closure includes types and barrel exports and therefore over-approximates runtime execution. Dynamic component/data navigation requires runtime confirmation. Exact locations, handlers, unresolved imports and per-page reachability are in [ui-workflows.json](ui-workflows.json) and [source-inventory.json](source-inventory.json).','', '## Layouts','',table(['Source','Rendered component/provider tags'],[(ref(s),', '.join(dict.fromkeys(x['tag'] for x in by_source[s]['jsx']))) for s in ui['layouts']]),'', '## Every page','']
for m,p in zip(matrix,ui['pages']):
    own=by_source[p['source']]
    calls=[c for c in own['calls'] if c['kind'] in ['auth','interaction','jsx']]
    parts += [f"### {m['id']} `{m['route']}`",'',m['workflow'],'',ref(m['source']), '', 'Inherited layouts: '+', '.join(ref(s) for s in m['layouts']), '', 'Direct local imports: '+(', '.join(ref(i['resolved']) for i in own['imports'] if i.get('resolved')) or 'none'), '', 'Page interaction sites: '+('; '.join(f"`{c['callee']}` at {c['line']}" for c in calls) or 'none in page AST; inspect imported component ledger'),'', 'Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.','']
parts += ['## All non-entry TSX components','', 'Scope includes 164 src/components TSX files and all route-scoped TSX plus supporting providers/layout helpers. Unreferenced components remain inventoried; no dead-code deletion is authorized.','',table(['Source','Declared symbols','Page reachability'],[(ref(c['source']),', '.join(dict.fromkeys(x['name'] for x in c['declarations'] if x['name'][0].isupper()))[:450] or '(anonymous/local declarations)',str(len(c['usedByPages']))+' source closures; see JSON') for c in ui['components']]),'', '## Hooks, contexts and providers','',table(['Source','Declarations','Page reachability'],[(ref(c['source']),', '.join(dict.fromkeys(x['name'] for x in c['declarations']))[:450],str(len(c['usedByPages']))) for c in ui['hooksAndProviders']]),'', '## Navigation sites','', 'This includes dynamic expressions and event handlers. Route constants and config object values also require review; see configuration references below. Literal targets are evidence candidates, not validation of their destination.','',table(['Source','Site','Literal/template target'],[(ref(n['source'],n['line']),n['callee'],n.get('target') or '(dynamic; see source)') for n in ui['navigation']]),'', 'Navigation configuration: '+', '.join(ref(s) for s in ['dozu-ui-service/src/utils/constants/routes.ts','dozu-ui-service/src/utils/auth/redirectService.ts','dozu-ui-service/src/configs/layout/list.config.ts','dozu-ui-service/src/components/side-bar/SideBar.tsx','dozu-ui-service/src/components/admin/Sidebar.tsx','dozu-ui-service/src/layouts/DefaultLayout.tsx'])]
write('ui-ledger.md','\n'.join(parts))

write('backend-endpoints.md','# Backend endpoint and business capability ledger\n\n330 unique method/path pairs beneath `/api`, derived from 52 reachable registered mounts (53 declarations; `/class_feeds` module is not reachable from API imports). Nested mounts preserve aliases. Add `GET /health` from '+ref('dozu-api-service/src/index.ts',57)+'. Eight explicit FastAPI endpoints are catalogued in systems.md; default OpenAPI/docs routes are additional.\n\nMethod, complete mounted URL, controller/handler chain, inherited middleware, import closure and source lines are available in [backend-endpoints.json](backend-endpoints.json). API version options are metadata: registerRoute does not automatically prepend `/v1`. Static middleware order is preserved; controller/service ownership checks still require request-level verification. No auth equivalence or endpoint success is claimed.\n\n'+table(['Method / mounted path','Handlers (including route-specific validation)','Earlier mounted middleware','Source'],[(e['method']+' `'+e['path']+'`','; '.join(e['handlers']),'; '.join(m['middleware'] for m in e['middlewareChain']),ref(e['source'],e['line'])) for e in api['endpoints']])+'\n\nUnreachable route declarations: '+', '.join(ref(s) for s in api['unreachableRouteFiles'])+'. The student class feed has separate nested mounts; do not treat the unused top-level module as removal of all feed behavior.')

envrows=[]
for name in config['environmentNames']:
    consumers=[c for c in config['consumers'] if c['name']==name]
    secret=any(x in name for x in ['SECRET','PASSWORD','TOKEN','API_KEY','ACCESS_KEY']) or name in ['DATABASE_URL','DATABASE_URL_DRIZZLE_MIGRATE']
    envrows.append((name,'sensitive/user-scoped or generated locally' if secret else 'configuration/public identifier; inspect use',', '.join(ref(c['source'],c['line']) for c in consumers)))
write('configuration.md','# Configuration, secret and external-consumer inventory\n\nSource-derived names only. No dotenv/token file values were read or copied. Existing dotenv paths are recorded separately in provenance. Database-backed provider base URLs/keys are additional configuration; environment scanning cannot enumerate stored values. Runtime readiness must tolerate missing optional provider credentials.\n\n'+table(['Name','Handling','Every source consumer'],envrows)+'\n\nLiteral host candidates (including documentation/test/example URLs) and source lines are in [configuration-inventory.json](configuration-inventory.json). They are not a packet capture or an exhaustive list of dynamic provider hosts. For classified live consumers and desktop options see [systems.md](systems.md).')

write('database.md','# Database and migration baseline\n\n'+f"{len(db['models'])} model/barrel files contain {sum(e['callee']=='pgTable' for m in db['models'] for e in m['entities'])} PostgreSQL table declarations and {sum(e['callee']=='pgEnum' for m in db['models'] for e in m['entities'])} enum declarations. "+'See [database-inventory.json](database-inventory.json) for every declaration, import dependency, journal entry and source hash.\n\n'+table(['Model/barrel','Entities'],[(ref(m['source']),', '.join(e['callee']+' '+e['name'] for e in m['entities'])) for m in db['models']])+'\n\n## Migration provenance\n\nAll 20 SQL migrations, their 20 journal entries and snapshot JSON files exist locally but are ignored by `drizzle/` and are absent from the source commit. A clean Git import loses them. Hashes preserve this local evidence without claiming an approved migration history.\n\n'+table(['Local migration','Tracked','SHA-256'],[(ref(m['source']),'yes' if m['tracked'] else '**NO — ignored local artifact**',m['sha256']) for m in db['migrations']])+'\n\nRuntime uses DATABASE_URL through pg/Drizzle; Drizzle tooling separately uses DATABASE_URL_DRIZZLE_MIGRATE and different dotenv selection. Bootstrap must reconcile these profiles, explicitly create pgvector before vector tables, apply reviewed migrations and seed roles/permissions/plans/features/LLM metadata without embedded keys. No migration was applied and no database/dump/user records were read.\n\nPostgreSQL-specific dependencies: enums, serial sequences, FK/cascade/unique constraints, timestamps/time zones, arrays/JSONB, `ILIKE`, PostgreSQL SQL fragments, `vector(384)` and HNSW cosine operators. '+ref('dozu-api-service/src/models/embedding/embedding.model.ts',21)+' and '+ref('dozu-api-service/src/repositories/embedding/embedding.repo.ts',113)+' anchor the vector contract. Local SQL migration 0013 creates vector/HNSW but the collected SQL has no CREATE EXTENSION statement. The container profiles reference PostgreSQL 16/17 without proving extension installation.\n\n`scripts/populate-test-data.ts` is a developer test-data script, not a clean-machine first-boot seed contract. Verify model/migration drift with a new disposable local cluster under #29/#40, including upgrades/rollback backup, missing FK data and unique-index behavior. SQLite is not a proven drop-in replacement.')

# Refresh the original route inventory without losing its source commit or layout/component arrays.
old=json.loads((ROOT/'planning/route-inventory.json').read_text(encoding='utf-8-sig'))
mapped={m['source']:m for m in matrix}
assert set(mapped)=={p['source'] for p in old['pages']}
for p in old['pages']:
    m=mapped[p['source']]
    p.update({'route':m['route'],'rolesAndWorkflows':m['rolesAndWorkflows'],'localRuntimeStatus':'Not implemented or verified; source audit complete','auditEvidence':'audit/feature-parity.json#'+m['id'],'followUpIssues':m['followUpIssues']})
old['auditDate']='2026-11-09'
old['auditStatus']='Source/workflow inventory audited; runtime desktop parity unverified'
(ROOT/'planning/route-inventory.json').write_text(json.dumps(old,indent=2)+'\n',encoding='utf-8')
(ROOT/'planning/route-inventory.md').write_text('# Complete route preservation inventory\n\nSource commit: `'+old['sourceCommit']+'`. Verified against current source: 84 pages, 20 layouts, 164 shared TSX files. Counts remain inventory, not passing parity. Route-scoped components/hooks/providers are additional.\n\nThe per-page workflow audit replaces the original placeholders:\n\n- [84-row feature-parity matrix](audit/feature-parity.md)\n- [All layouts/components/hooks/providers/navigation and page interactions](audit/ui-ledger.md)\n- [Machine-readable original inventory](route-inventory.json)\n- [Baseline audit and limitations](audit/README.md)\n\nAll desktop runtime parity remains unverified. No source page was removed or migrated.\n',encoding='utf-8')
print(json.dumps({'pages':len(matrix),'components':len(ui['components']),'hooksAndProviders':len(ui['hooksAndProviders']),'navigationSites':len(ui['navigation']),'apiEndpoints':len(api['endpoints']),'models':len(db['models']),'migrations':len(db['migrations']),'environmentNames':len(config['environmentNames'])}))
