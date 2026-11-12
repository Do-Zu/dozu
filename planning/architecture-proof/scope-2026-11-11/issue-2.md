<!-- dozu-tracking:start -->
## Work tracking
Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.

**Planning complexity:** M - Requirements and a complete role/route matrix; bounded documentation with product decisions.
Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.
**Planning priority:** P0 - Architecture/foundation work that unblocks the implementation path.
<!-- dozu-tracking:end -->

## Outcome
Record the now-fixed local-first architecture, full UI scope and supported platform matrix. Internet-enabled integrations remain in scope; do not reopen online-first versus offline-only as the architecture choice.

## Acceptance criteria
- [x] Record local frontend/backend/database/files, optional internet APIs, no required central application server/cloud DB/sync and self-contained install as mandatory.
- [x] Build a per-route/role/locale/feature matrix from all 84 current page entrypoints, 20 layouts, 164 shared TSX components and route-scoped code; update counts if sources change.
- [x] Include all admin, teacher/student, payment/history, auth, generation, media, games, study, schedule/settings and navigation flows; no silent omissions.
- [x] Agree OS minimum versions, CPU architectures, Linux distro baseline, installer types and resource budgets.
- [x] Record public callback/shared-secret/classroom topology decisions under INTEGRATIONS; preserve actual external functionality wherever feasible.

## Architecture constraints
The complete existing Next.js UI and Express backend run locally with a local database/files. Desktop and local browser use the same localhost backend. Real third-party integrations may use the internet; preserve them wherever feasible. No central Dozu backend, cloud database, synchronization, shared publisher secrets in installers, or simulated replacements. All pages/features remain in release scope.

<!-- dozu-roadmap:DECISION-SCOPE -->

Phase: 0 Requirements | Priority: P0

Parent roadmap: https://github.com/Do-Zu/dozu/issues/1

## Dependencies
None; this work can start independently.


## Requirements evidence — 2026-11-10

The local-first architecture and complete feature scope are mandatory. The Task #3 source commits remain unchanged. Local evidence: `planning/requirements.md`, `planning/feature-preservation.md/json`, `planning/platform-support.md`, `planning/integration-decisions.md`, and the immutable `planning/audit/` ledgers. These files are in the current checkout and have not been pushed. The page scope is reproduced below for GitHub review.

Source coverage verified against tracked UI commit `5e1ceb263a29e2fde2359c36f43d0118a8d622f0`: **84 pages, 20 layouts, 164 shared TSX components**. The expanded audit covers 584 non-entry TSX (including the 164), 132 hook/provider/context sources and 550 navigation/config sites. All route-scoped code remains in scope. Family counts: public/diagnostic 5, classroom 26, administration 18, accounts 7, generation/Feynman 2, study workspace 15, personal learning 8, billing 1, teacher approval 2.

Required surfaces: retained website build, packaged Electron and localhost browser sharing the local Express/database/files stack. Each applicable workflow must preserve en/vi, layouts/themes, authorized and denied access, mutations/local persistence/restart, loading/empty/validation/error/retry states, provider missing/offline/failure/real-success behavior, and files/streams/sockets/media. These are implementation acceptance requirements, **not passing runtime results**. Existing placeholders, missing navigation destinations and baseline failures remain tracked gaps; no page or feature is removed.

**Agreement still required:** minimum Windows/macOS versions, CPU targets, Linux distro/release baseline, installer formats, RAM/disk/installer-size/cold-and-warm-start/CPU budgets; merchant ownership (#41); and classroom participant topology (#43). Windows/macOS/Linux remain intended families. Developer host versions are not support commitments. The #27 record distinguishes established constraints from proposed provider/callback flows. No numeric defaults, ownership or topology are invented. Do not close #2 until the remaining choices are agreed and recorded. Runtime proof stays in downstream implementation issues.

<details>
<summary>All 84 required pages — en/vi; roles below are source intent, not authorization proof</summary>

| ID / family | Route and source | Role intent | Existing required workflow |
| --- | --- | --- | --- |
| UI-001 / Public and diagnostic | [`/[locale]/about`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/about/page.tsx) | public/redirect/developer surface | Read team/profile content. |
| UI-002 / Classroom | [`/[locale]/activities/join/[activityId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/activities/join/%5BactivityId%5D/page.tsx) | student/participant intent | Join quiz activity, show availability/status and start navigation. |
| UI-003 / Administration | [`/[locale]/admin/features`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/features/page.tsx) | admin intent | List/create/update/delete subscription features and limits. |
| UI-004 / Administration | [`/[locale]/admin/feedback`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/feedback/page.tsx) | admin intent | Filter/list feedback and update moderation/status/auto-ignore operations. |
| UI-005 / Administration | [`/[locale]/admin/llm-api-key-models`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/llm-api-key-models/page.tsx) | admin intent | Create/edit/delete key-model associations, priorities and quotas. |
| UI-006 / Administration | [`/[locale]/admin/llm-api-keys`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/llm-api-keys/page.tsx) | admin intent | Create/edit/delete/filter provider keys and key status; sensitive DB-backed key handling. |
| UI-007 / Administration | [`/[locale]/admin/llm-models`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/llm-models/page.tsx) | admin intent | Create/edit/delete/filter provider models and availability. |
| UI-008 / Administration | [`/[locale]/admin/llm-providers`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/llm-providers/page.tsx) | admin intent | Create/edit/delete/filter providers, URLs and availability. |
| UI-009 / Administration | [`/[locale]/admin`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/page.tsx) | admin intent | Account/role/activity dashboard cards and signup chart. |
| UI-010 / Administration | [`/[locale]/admin/payments`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/payments/page.tsx) | admin intent | Filter/page payment ledger and export CSV. |
| UI-011 / Administration | [`/[locale]/admin/plans/[planId]/features`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/plans/%5BplanId%5D/features/page.tsx) | admin intent | Assign/edit/remove plan feature access and limits. |
| UI-012 / Administration | [`/[locale]/admin/plans`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/plans/page.tsx) | admin intent | List/create/edit/delete plans and navigate feature assignment. |
| UI-013 / Administration | [`/[locale]/admin/revenue`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/revenue/page.tsx) | admin intent | Filter revenue and gateway/plan/trend analytics. |
| UI-014 / Administration | [`/[locale]/admin/stats`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/stats/page.tsx) | admin intent | Fetch user statistics and render charts/loading state. |
| UI-015 / Administration | [`/[locale]/admin/subscriptions/list`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/subscriptions/list/page.tsx) | admin intent | Filter/page subscription records and administer their states. |
| UI-016 / Administration | [`/[locale]/admin/subscriptions`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/subscriptions/page.tsx) | admin intent | Subscription KPI/status/monthly charts with links to lists/plans/features. |
| UI-017 / Administration | [`/[locale]/admin/teacher-requests`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/teacher-requests/page.tsx) | admin intent | List teacher applications/statuses. |
| UI-018 / Administration | [`/[locale]/admin/teacher-requests/pending`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/teacher-requests/pending/page.tsx) | admin intent | Review pending applications and approve/reject. |
| UI-019 / Administration | [`/[locale]/admin/users/[id]/oauth`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/users/%5Bid%5D/oauth/page.tsx) | admin intent | Read user linked authentication accounts and provider metadata. |
| UI-020 / Administration | [`/[locale]/admin/users`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/admin/users/page.tsx) | admin intent | Filter/page users; activate/deactivate, edit role and inspect OAuth associations. |
| UI-021 / Accounts | [`/[locale]/auth/changePassword`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/auth/changePassword/page.tsx) | guest/account/link callback | Validate email/code query and submit new password. |
| UI-022 / Accounts | [`/[locale]/auth/changePasswordEmailSent`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/auth/changePasswordEmailSent/page.tsx) | guest/account/link callback | Show delivery guidance and return navigation; not proof of email delivery. |
| UI-023 / Accounts | [`/[locale]/auth/forgotPassword`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/auth/forgotPassword/page.tsx) | guest/account/link callback | Request password-change email and show sent/error state. |
| UI-024 / Accounts | [`/[locale]/auth/login`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/auth/login/page.tsx) | guest/account/link callback | Password sign-in; real Google code redirect; preserve redirect destination and error/loading states. |
| UI-025 / Accounts | [`/[locale]/auth/register`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/auth/register/page.tsx) | guest/account/link callback | Create account, verification mail, Google sign-in, validation and login link. |
| UI-026 / Accounts | [`/[locale]/auth/testBackEnd`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/auth/testBackEnd/page.tsx) | guest/account/link callback | Developer authentication/Redux test surface; preserve source, classify for release. |
| UI-027 / Accounts | [`/[locale]/auth/verifyEmail`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/auth/verifyEmail/page.tsx) | guest/account/link callback | Read email/code query, verify with backend, update session and navigate. |
| UI-028 / Public and diagnostic | [`/[locale]/blogs`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/blogs/page.tsx) | public/redirect/developer surface | Render Blog Page heading; placeholder, no blog CRUD. |
| UI-029 / Classroom | [`/[locale]/class-based/[id]/assignments/[assignmentId]/details`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/class-based/%5Bid%5D/assignments/%5BassignmentId%5D/details/page.tsx) | student/participant intent | Read assignment/attachments/comments; student uploads/replaces/submits work and reads private feedback. |
| UI-030 / Classroom | [`/[locale]/class-based/[id]/class-quiz/[classQuizId]/history`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/class-based/%5Bid%5D/class-quiz/%5BclassQuizId%5D/history/page.tsx) | student/participant intent | List/review student attempt history with answers and timing. |
| UI-031 / Classroom | [`/[locale]/class-based/[id]/class-quiz/[classQuizId]/start`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/class-based/%5Bid%5D/class-quiz/%5BclassQuizId%5D/start/page.tsx) | student/participant intent | Student start timed attempt, autosave answers, receive quiz activity and confirm submit. |
| UI-032 / Classroom | [`/[locale]/class-based/[id]/class-quiz/[classQuizId]/submit`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/class-based/%5Bid%5D/class-quiz/%5BclassQuizId%5D/submit/page.tsx) | student/participant intent | Submit/review attempt and show result; preserve deadline/retry semantics. |
| UI-033 / Classroom | [`/[locale]/class-based/[id]/learning-material/[learningMaterialId]/details`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/class-based/%5Bid%5D/learning-material/%5BlearningMaterialId%5D/details/page.tsx) | student/participant intent | Read material content/attachments/comments; student read/comment actions. |
| UI-034 / Classroom | [`/[locale]/class-based/[id]/mindmap/[topicId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/class-based/%5Bid%5D/mindmap/%5BtopicId%5D/page.tsx) | student/participant intent | Class topic ReactFlow mindmap, source and flashcard sheets, export; student read-only access. |
| UI-035 / Classroom | [`/[locale]/class-based/[id]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/class-based/%5Bid%5D/page.tsx) | student/participant intent | Student dashboard tabs: topics, feed, classwork/materials, assignments and quizzes. |
| UI-036 / Classroom | [`/[locale]/class-based/[id]/topics/[topicId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/class-based/%5Bid%5D/topics/%5BtopicId%5D/page.tsx) | student/participant intent | Class context wraps shared topic workspace and mindmap provider; preserve teacher/student permissions across tabs. |
| UI-037 / Classroom | [`/[locale]/class-based`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/class-based/page.tsx) | student/participant intent | Student class library, invitation/join and class navigation. |
| UI-038 / Generation and Feynman | [`/[locale]/feynman/[topicId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/feynman/%5BtopicId%5D/page.tsx) | authenticated | Read mission/source, write explanation, request genuine AI questions/review, view history and save learning progress. |
| UI-039 / Study workspace | [`/[locale]/games/brain-chase`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/games/brain-chase/page.tsx) | account/topic ownership intent | Flashcard-based game, pause/restart/settings and result/progress integration. |
| UI-040 / Study workspace | [`/[locale]/games/memory-match`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/games/memory-match/page.tsx) | account/topic ownership intent | Match flashcard pairs, timer/game state and completion behavior. |
| UI-041 / Generation and Feynman | [`/[locale]/generate`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/generate/page.tsx) | authenticated | Choose text/file/URL/YouTube/media input, convert/transcribe, select model/content/difficulty, stream generation, preview/save study content. |
| UI-042 / Personal learning | [`/[locale]/home`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/home/page.tsx) | guest preview or authenticated personal data | Guest preview or account library; packages/tree/topics CRUD, current learning, generate actions, learning-mode/admin redirects. |
| UI-043 / Study workspace | [`/[locale]/mindmap/[topicId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/mindmap/%5BtopicId%5D/page.tsx) | account/topic ownership intent | Edit ReactFlow nodes/edges, flashcards/source sheet, generation, roadmap and export/import/save actions. |
| UI-044 / Study workspace | [`/[locale]/mindmap/add-flashcard`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/mindmap/add-flashcard/page.tsx) | account/topic ownership intent | Select flashcards in table and attach to nodes; verify IDs/save integration. |
| UI-045 / Study workspace | [`/[locale]/mindmap/nodes/[id]/flashcard`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/mindmap/nodes/%5Bid%5D/flashcard/page.tsx) | account/topic ownership intent | Temporary node flashcard list fetched through raw Axios; loading/empty/error states. |
| UI-046 / Study workspace | [`/[locale]/mindmap/nodes/[id]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/mindmap/nodes/%5Bid%5D/page.tsx) | account/topic ownership intent | Mostly empty node page with parameter check; ReactFlow body commented out. |
| UI-047 / Study workspace | [`/[locale]/mindmap/view/[topicId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/mindmap/view/%5BtopicId%5D/page.tsx) | account/topic ownership intent | View-only ReactFlow source/node sheets and export/download. |
| UI-048 / Personal learning | [`/[locale]/onboarding`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/onboarding/page.tsx) | guest preview or authenticated personal data | Step through topic tags, duration and learning-method preferences; persist completion. |
| UI-049 / Public and diagnostic | [`/[locale]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/page.tsx) | public/redirect/developer surface | Choose redirect by account/onboarding state; show auth loading. |
| UI-050 / Billing | [`/[locale]/payment`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/payment/page.tsx) | authenticated | Select plan/payment method, genuine checkout/QR, cancel/return, realtime result and transaction status/history. |
| UI-051 / Personal learning | [`/[locale]/profile`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/profile/page.tsx) | guest preview or authenticated personal data | Load/update personal information, avatar and notification/settings tabs. |
| UI-052 / Personal learning | [`/[locale]/progress`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/progress/page.tsx) | guest preview or authenticated personal data | Progress dashboard with study totals and topic/method progress. |
| UI-053 / Study workspace | [`/[locale]/question/edit/[topicId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/question/edit/%5BtopicId%5D/page.tsx) | account/topic ownership intent | Question editor: change questions/answers/options and persist topic quiz bank. |
| UI-054 / Study workspace | [`/[locale]/quiz/[topicId]/doing`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/quiz/%5BtopicId%5D/doing/page.tsx) | account/topic ownership intent | Answer quiz, navigate questions, confirm submission and persist results. |
| UI-055 / Study workspace | [`/[locale]/quiz/[topicId]/history/[quizResultId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/quiz/%5BtopicId%5D/history/%5BquizResultId%5D/page.tsx) | account/topic ownership intent | Read historical attempt questions/answers and scoring details. |
| UI-056 / Study workspace | [`/[locale]/quiz/[topicId]/history`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/quiz/%5BtopicId%5D/history/page.tsx) | account/topic ownership intent | List attempts and open result/history details. |
| UI-057 / Study workspace | [`/[locale]/quiz/[topicId]/result/[quizResultId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/quiz/%5BtopicId%5D/result/%5BquizResultId%5D/page.tsx) | account/topic ownership intent | Display saved result and review answers. |
| UI-058 / Study workspace | [`/[locale]/quiz/local`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/quiz/local/page.tsx) | account/topic ownership intent | Browser-storage quiz draft/answers plus streak update; shared DB authority requires explicit transfer contract. |
| UI-059 / Teacher approval | [`/[locale]/request-teacher`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/request-teacher/page.tsx) | authenticated account intent | Read request status or submit teacher application. |
| UI-060 / Teacher approval | [`/[locale]/request-teacher/reapply`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/request-teacher/reapply/page.tsx) | authenticated account intent | Edit/resubmit teacher application after rejection. |
| UI-061 / Personal learning | [`/[locale]/schedule`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/schedule/page.tsx) | guest preview or authenticated personal data | Calendar/list views, recommended slots and learning progress interactions. |
| UI-062 / Personal learning | [`/[locale]/setting/profile`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/setting/profile/page.tsx) | guest preview or authenticated personal data | Authenticated wrapper reusing profile page. |
| UI-063 / Personal learning | [`/[locale]/setting/schedule-setup`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/setting/schedule-setup/page.tsx) | guest preview or authenticated personal data | Configure study availability, frequency, methods and schedule preferences. |
| UI-064 / Personal learning | [`/[locale]/stats`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/stats/page.tsx) | guest preview or authenticated personal data | LearningProgress component; verify supplied data and API use before claiming analytics. |
| UI-065 / Classroom | [`/[locale]/teacher/class-based/[id]/activities/[activityId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/activities/%5BactivityId%5D/page.tsx) | teacher intent | Teacher live quiz monitoring tabs, participation/answer events, refresh and XLSX results export. |
| UI-066 / Classroom | [`/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/assignments/%5BassignmentId%5D/details/page.tsx) | teacher intent | Read assignment/attachments/comments; teacher reviews/grades submissions and edits/deletes assignment. |
| UI-067 / Classroom | [`/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/edit`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/assignments/%5BassignmentId%5D/edit/page.tsx) | teacher intent | Load/edit assignment, topics, rich text, attachments and scheduling. |
| UI-068 / Classroom | [`/[locale]/teacher/class-based/[id]/assignments`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/assignments/page.tsx) | teacher intent | Create assignment, choose class/topics, rich text, attachments and scheduling; persist and return to class. |
| UI-069 / Classroom | [`/[locale]/teacher/class-based/[id]/class-quiz/[classQuizId]/edit`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/class-quiz/%5BclassQuizId%5D/edit/page.tsx) | teacher intent | Edit quiz draft/questions/settings and publish/schedule/close lifecycle. |
| UI-070 / Classroom | [`/[locale]/teacher/class-based/[id]/class-quiz`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/class-quiz/page.tsx) | teacher intent | List teacher quiz drafts/publications and navigate editing. |
| UI-071 / Classroom | [`/[locale]/teacher/class-based/[id]/generate`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/generate/page.tsx) | teacher intent | Teacher generation reuses full GeneratePage for class/topic content. |
| UI-072 / Classroom | [`/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/details`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/learning-material/%5BlearningMaterialId%5D/details/page.tsx) | teacher intent | Read material content/attachments/comments; teacher edit/delete actions. |
| UI-073 / Classroom | [`/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/edit`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/learning-material/%5BlearningMaterialId%5D/edit/page.tsx) | teacher intent | Load/edit teaching material, content, attachments and associated topics. |
| UI-074 / Classroom | [`/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/learning-material/%5BlearningMaterialId%5D/page.tsx) | teacher intent | Read/download learning-material attachment from backend. |
| UI-075 / Classroom | [`/[locale]/teacher/class-based/[id]/learning-material`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/learning-material/page.tsx) | teacher intent | Create teaching material with topic/content/attachment selection. |
| UI-076 / Classroom | [`/[locale]/teacher/class-based/[id]/mindmap/[topicId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/mindmap/%5BtopicId%5D/page.tsx) | teacher intent | Class topic ReactFlow mindmap, source and flashcard sheets, export; teacher edit/save/generate actions. |
| UI-077 / Classroom | [`/[locale]/teacher/class-based/[id]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/page.tsx) | teacher intent | Teacher class dashboard, topics/feed/classwork tabs, create/edit/archive and access management. |
| UI-078 / Classroom | [`/[locale]/teacher/class-based/[id]/students`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/students/page.tsx) | teacher intent | List/search student enrollment, profile modal and enrollment management. |
| UI-079 / Classroom | [`/[locale]/teacher/class-based/[id]/topics/[topicId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/class-based/%5Bid%5D/topics/%5BtopicId%5D/page.tsx) | teacher intent | Class context wraps shared topic workspace and mindmap provider; preserve teacher/student permissions across tabs. |
| UI-080 / Classroom | [`/[locale]/teacher/home`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/teacher/home/page.tsx) | teacher intent | Teacher class library and class management/navigation. |
| UI-081 / Public and diagnostic | [`/[locale]/tests/class/comment`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/tests/class/comment/page.tsx) | public/redirect/developer surface | Empty developer route; not implemented comment UI. |
| UI-082 / Study workspace | [`/[locale]/topics/[topicId]`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/topics/%5BtopicId%5D/%28topic%29/page.tsx) | account/topic ownership intent | Topic workspace tabs for flashcards, quiz, mindmap, notes and media; generation/edit/learning and source-linked context. |
| UI-083 / Study workspace | [`/[locale]/topics/[topicId]/settings/anki`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/topics/%5BtopicId%5D/settings/anki/page.tsx) | account/topic ownership intent | Select/create/update/delete Anki preset, edit parameters, assign to topic and reset defaults. |
| UI-084 / Public and diagnostic | [`/[locale]/welcome`](https://github.com/perinst/dozu-ui-service/blob/5e1ceb263a29e2fde2359c36f43d0118a8d622f0/src/app/%5Blocale%5D/welcome/page.tsx) | public/redirect/developer surface | Browse landing/FAQ, change language/theme and enter sign-in/onboarding. |

</details>

## User-approved v1 decisions — 2026-11-10

The user has supplied the v1 support contract. This supersedes the earlier pending-decision note. These are requirements and engineering targets, not measured results.

## OS, architecture and distribution

| Platform | Required v1 baseline | CPU | Installer |
| --- | --- | --- | --- |
| Windows | Windows 10 22H2, legacy compatibility; Windows 11, primary | x86-64 | NSIS .exe primary; .msi optional for enterprise |
| macOS | macOS 13 Ventura or later | Intel x86-64 and Apple Silicon ARM64 | Signed and notarized .dmg for each architecture |
| Linux | Ubuntu 22.04 LTS and Debian 12 minimum tested baselines; Ubuntu 24.04 LTS or newer recommended | x86-64 | .deb for Ubuntu/Debian; additional .AppImage where compatible |

32-bit systems are unsupported. Windows ARM64 and Linux ARM64 may be added only after native dependency validation; they are not current required v1 targets. Later recommended releases still require compatibility evidence; the wording above does not assert tests have run.

## Hardware

| Configuration | CPU | System RAM | Free disk | Display / storage |
| --- | --- | --- | --- | --- |
| Minimum | 64-bit dual-core | 4 GB | 2 GB for installation and initial data | 1366 × 768; integrated graphics; HDD-compatible, SSD preferred |
| Recommended | 64-bit quad-core or better | 8 GB or more | 5 GB | 1920 × 1080; SSD |
| High performance | 6–8+ cores | 16 GB or more | Dataset/workload-dependent; no additional number specified | NVMe SSD; larger datasets and concurrent background workloads |

A dedicated GPU is not required for normal functionality. Provide a low-resource mode for 4 GB machines using efficient process management, lazy initialization, bounded caching and reduced background concurrency. Preserve functionality; do not achieve budgets by silently removing pages or required processing.

## Performance and disk targets

| Production-build metric | Minimum-spec device | Recommended device |
| --- | --- | --- |
| Cold launch to interactive UI | ≤ 10 s | ≤ 5 s |
| Warm launch to interactive UI | ≤ 5 s | ≤ 3 s |
| Local backend ready | ≤ 8 s | ≤ 4 s |
| Normal application memory, including backend and database | ≤ 700 MB | ≤ 1 GB |

Installer target: **≤ 250 MB**. Installed application target, including bundled backend: **≤ 750 MB**. Require **at least 2 GB free before installation**, covering installation and initial data. User-generated data and imported media may grow beyond the application footprint. Account for runtime/model/assets in the application footprint; do not hide them in a first-run download or call them user data to satisfy the budget.

Use production builds and documented repeatable workloads on minimum supported configurations. Document OS/CPU/RAM/storage, dataset/media sizes, model revision, cache state, concurrency, network state and measurement method. Report all resident app-owned processes, including Electron, Next, API, database and any running embedding/converter/transcription processes. Keep interactive-UI and backend-ready timings separate; an interactive shell is not proof the database/model is ready. Measure background and processing peaks as well as the agreed normal workload. No numerical CPU cap, conversion/embedding peak-memory cap or peak upgrade-space budget was supplied; measure and report them rather than inventing an agreement.

## Local runtime and data lifecycle

Backend and primary data storage run locally. Internet is permitted for genuine Google authentication, email, YouTube and other external services; classroom v1 is LAN, and payments are explicitly deferred/blocked under #41. No externally hosted application backend is required for core local functionality. Bundle/provision required dependencies through installation; no manual Node, Python, database, Docker, WSL or developer tooling. Retain the earlier self-contained baseline model/runtime requirement.

PostgreSQL/pgvector remains the source-supported candidate. The user permits considering SQLite **only after compatibility with the existing backend/business requirements is validated**. This does not authorize a database replacement: #4/#29 must prove migrations, PostgreSQL-specific SQL/JSONB, vector(384)/cosine/HNSW behavior and repository contracts before recommending an alternative.

Upgrades preserve data. Uninstall retains the earlier explicit keep-data/delete-all-app-owned-data choice, with reliable removal of app-owned databases, caches, logs and local data while protecting unrelated files. All managed data stays on the device unless the feature explicitly requires external communication. LAN participants access the user-owned host's authoritative data; no cloud database/sync is introduced.

## Evidence gates

#4/#38 must prove each agreed native OS/CPU combination and resource budget; #21/#32 include all media/conversion/transcription/model/font/browser resources discovered by audit. Electron + Next + Express + PostgreSQL + Python/model and conversion resources have not yet been shown to fit these budgets. No target is relaxed based on that uncertainty.

#22/#23/#25/#33/#35/#36 validate clean installation, startup/readiness, memory/core functionality, dependency compatibility, low-resource mode, restart/recovery, upgrades/backup/restore and uninstall on the minimum configurations. Release compliance requires actual evidence. Signing/distribution remain #24/#26. A benchmark failure requires evidence and an explicit recommendation before changing this contract.


Payment decision: explicitly defer/skip payment execution and retain existing issue #41 as the single blocker. Merchant ownership is deferred, not selected. Preserve page/history inventory and a clear disabled/unavailable payment state when implemented; no live charges, fake success or payment-page deletion. This is an explicit scope exception to earlier all-feature wording.

Classroom decision: other devices on the same LAN use a user-owned authoritative local host. Preserve teacher/student workflows with explicit LAN access/auth/TLS/availability proof under #43. Remote internet/tunnel participants are not a v1 requirement. No central Dozu backend/cloud database/sync.

All five #2 criteria are now evidenced as requirements. Implementation, installer/platform compatibility, performance/resource benchmarks, provider flows, data lifecycle and LAN runtime proof remain open under downstream issues. Source trees remain unchanged.

<!-- dozu-v1-scope-2026-11-11:start -->
## User-approved v1 scope amendment — 2026-11-11

- Remove local speech-to-text from this version: no whisper.cpp server, tiny speech model, speech startup/readiness gate or speech-only assets. Retain independent media playback and genuine existing YouTube transcript text retrieval. Preserve source/page inventory; no fake transcript or new cloud STT fallback.
- Keep PostgreSQL; **defer pgvector**. A private relational cluster, reviewed migrations/seeds, persistence and data-safe upgrades remain required. Current vector(384), `<=>` and HNSW consumers need explicit reviewed adaptation; do not blindly run vector-dependent migrations, discard data or replace PostgreSQL.
- The measured 479.729 MB MiniLM snapshot is a separate **text-embedding model**, used by retained PDF/YouTube reference search and ingestion. The user's condition for dropping its experiment is not met: keep smaller-runtime/quantization proof scoped to these consumers. No working smaller runtime or pgvector-free ranking implementation is claimed.
- Ordinary PostgreSQL array/JSONB vector storage plus bounded application-side cosine ranking is an evaluation candidate only. Prove owner/topic filtering, 384-value shape, ranking/topK/ties, persistence/migration, quality and realistic scale/resource budgets before adopting it. Semantic reference retrieval has not been deferred by this decision.
- Exclude FFmpeg only when its sole consumer is deferred speech-to-text; separately prove any retained non-STT need. Keep required document/URL/PDF/editor/media/font/browser resources. OS/CPU/installers, 250 MB installer/750 MB installed and memory/startup targets remain unchanged. Payments remain deferred under #41; classrooms remain LAN.

Source trace: `PdfFileEmbeddingStrategy.ts`, `YoutubeEmbeddingStrategy.ts`, `BaseEmbeddingStrategy.queryTopSimilarity()`, `inputSet.service.ts`, UI topic `components/reference/Reference.tsx`, and separate `features/whisper/api/whisper.service.ts`. Full record: local `planning/v1-scope-2026-11-11.md`. Earlier audits/measurements are historical evidence. Planning updates are not implemented feature removal or passing acceptance.
<!-- dozu-v1-scope-2026-11-11:end -->
