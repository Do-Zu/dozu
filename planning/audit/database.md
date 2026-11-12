# Database and migration baseline

74 model/barrel files contain 72 PostgreSQL table declarations and 27 enum declarations. See [database-inventory.json](database-inventory.json) for every declaration, import dependency, journal entry and source hash.

| Model/barrel | Entities |
| --- | --- |
| [dozu-api-service/src/models/anki-setting/ankiSetting.model.ts:1](<../../dozu-api-service/src/models/anki-setting/ankiSetting.model.ts#L1>) | pgTable anki_settings |
| [dozu-api-service/src/models/attachment.model.ts:1](<../../dozu-api-service/src/models/attachment.model.ts#L1>) | pgTable attachment |
| [dozu-api-service/src/models/auth/authAccount.model.ts:1](<../../dozu-api-service/src/models/auth/authAccount.model.ts#L1>) | pgTable auth_accounts |
| [dozu-api-service/src/models/auth/changePasswordRequest.model.ts:1](<../../dozu-api-service/src/models/auth/changePasswordRequest.model.ts#L1>) | pgTable change_password_requests |
| [dozu-api-service/src/models/auth/emailVerificationCode.model.ts:1](<../../dozu-api-service/src/models/auth/emailVerificationCode.model.ts#L1>) | pgTable email_verification_codes |
| [dozu-api-service/src/models/auth/permission.model.ts:1](<../../dozu-api-service/src/models/auth/permission.model.ts#L1>) | pgTable permissions |
| [dozu-api-service/src/models/auth/role.model.ts:1](<../../dozu-api-service/src/models/auth/role.model.ts#L1>) | pgTable roles |
| [dozu-api-service/src/models/auth/rolePermission.model.ts:1](<../../dozu-api-service/src/models/auth/rolePermission.model.ts#L1>) | pgTable role_permissions |
| [dozu-api-service/src/models/auth/userRole.model.ts:1](<../../dozu-api-service/src/models/auth/userRole.model.ts#L1>) | pgTable user_roles |
| [dozu-api-service/src/models/class-based-learning/assignment/assignment.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/assignment/assignment.model.ts#L1>) | pgEnum assignment_status_type, pgTable assignments |
| [dozu-api-service/src/models/class-based-learning/assignment/assignmentAttachments.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/assignment/assignmentAttachments.model.ts#L1>) | pgTable assignment_attachments |
| [dozu-api-service/src/models/class-based-learning/assignment/assignmentComment.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/assignment/assignmentComment.model.ts#L1>) | pgTable assignment_comments |
| [dozu-api-service/src/models/class-based-learning/assignment/assignmentSubmission.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/assignment/assignmentSubmission.model.ts#L1>) | pgEnum submission_status_type, pgTable assignment_submissions |
| [dozu-api-service/src/models/class-based-learning/assignment/assignmentSubmissionAttachments.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/assignment/assignmentSubmissionAttachments.model.ts#L1>) | pgTable assignment_submission_attachments |
| [dozu-api-service/src/models/class-based-learning/assignment/index.ts:1](<../../dozu-api-service/src/models/class-based-learning/assignment/index.ts#L1>) |  |
| [dozu-api-service/src/models/class-based-learning/class.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/class.model.ts#L1>) | pgTable classes |
| [dozu-api-service/src/models/class-based-learning/classEnrollment.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/classEnrollment.model.ts#L1>) | pgTable class_enrollments |
| [dozu-api-service/src/models/class-based-learning/classFeed.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/classFeed.model.ts#L1>) | pgEnum feed_type, pgTable class_feeds |
| [dozu-api-service/src/models/class-based-learning/classInvite.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/classInvite.model.ts#L1>) | pgEnum invite_status, pgTable class_invites |
| [dozu-api-service/src/models/class-based-learning/classTopicComment.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/classTopicComment.model.ts#L1>) | pgTable class_topic_comments |
| [dozu-api-service/src/models/class-based-learning/quiz-class/classQuizAttemptAnswers.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/quiz-class/classQuizAttemptAnswers.model.ts#L1>) | pgTable class_quiz_attempt_answers |
| [dozu-api-service/src/models/class-based-learning/quiz-class/classQuizAttempts.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/quiz-class/classQuizAttempts.model.ts#L1>) | pgEnum class_quiz_attempt_status, pgTable class_quiz_attempts |
| [dozu-api-service/src/models/class-based-learning/quiz-class/classQuizDraft.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/quiz-class/classQuizDraft.model.ts#L1>) | pgTable class_quiz_drafts |
| [dozu-api-service/src/models/class-based-learning/quiz-class/classQuizVersions.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/quiz-class/classQuizVersions.model.ts#L1>) | pgTable class_quiz_versions |
| [dozu-api-service/src/models/class-based-learning/quiz-class/classQuizzes.model.ts:1](<../../dozu-api-service/src/models/class-based-learning/quiz-class/classQuizzes.model.ts#L1>) | pgEnum class_quiz_status, pgTable class_quizzes |
| [dozu-api-service/src/models/comment/comment.model.ts:1](<../../dozu-api-service/src/models/comment/comment.model.ts#L1>) | pgTable comments |
| [dozu-api-service/src/models/demo.model.ts:1](<../../dozu-api-service/src/models/demo.model.ts#L1>) | pgTable demo |
| [dozu-api-service/src/models/embedding/embedding.model.ts:1](<../../dozu-api-service/src/models/embedding/embedding.model.ts#L1>) | pgTable embeddings |
| [dozu-api-service/src/models/embedding/index.ts:1](<../../dozu-api-service/src/models/embedding/index.ts#L1>) |  |
| [dozu-api-service/src/models/feedback/feedback.model.ts:1](<../../dozu-api-service/src/models/feedback/feedback.model.ts#L1>) | pgEnum feedback_status, pgEnum feedback_category, pgTable feedback |
| [dozu-api-service/src/models/feynman/feynman.model.ts:1](<../../dozu-api-service/src/models/feynman/feynman.model.ts#L1>) | pgTable feynman_sessions |
| [dozu-api-service/src/models/feynman/index.ts:1](<../../dozu-api-service/src/models/feynman/index.ts#L1>) |  |
| [dozu-api-service/src/models/flashcard.model.ts:1](<../../dozu-api-service/src/models/flashcard.model.ts#L1>) | pgTable flashcards |
| [dozu-api-service/src/models/flashcardBacklog.model.ts:1](<../../dozu-api-service/src/models/flashcardBacklog.model.ts#L1>) | pgEnum backlog_source, pgEnum backlog_status, pgTable flashcard_backlog_items |
| [dozu-api-service/src/models/gamification/achievement.model.ts:1](<../../dozu-api-service/src/models/gamification/achievement.model.ts#L1>) | pgTable achievements, pgTable user_achievements |
| [dozu-api-service/src/models/gamification/class-streaks.model.ts:1](<../../dozu-api-service/src/models/gamification/class-streaks.model.ts#L1>) | pgTable class_streaks |
| [dozu-api-service/src/models/gamification/points.model.ts:1](<../../dozu-api-service/src/models/gamification/points.model.ts#L1>) | pgTable points, pgTable point_transactions |
| [dozu-api-service/src/models/gamification/streak-events.model.ts:1](<../../dozu-api-service/src/models/gamification/streak-events.model.ts#L1>) | pgTable streak_events |
| [dozu-api-service/src/models/index.ts:1](<../../dozu-api-service/src/models/index.ts#L1>) |  |
| [dozu-api-service/src/models/inputSet.model.ts:1](<../../dozu-api-service/src/models/inputSet.model.ts#L1>) | pgTable input_set |
| [dozu-api-service/src/models/learning-material/attachmentInLearningMaterial.model.ts:1](<../../dozu-api-service/src/models/learning-material/attachmentInLearningMaterial.model.ts#L1>) | pgTable attachment_in_learning_material |
| [dozu-api-service/src/models/learning-material/learningMaterial.model.ts:1](<../../dozu-api-service/src/models/learning-material/learningMaterial.model.ts#L1>) | pgTable learning_materials |
| [dozu-api-service/src/models/learning-material/learningMaterialComment.model.ts:1](<../../dozu-api-service/src/models/learning-material/learningMaterialComment.model.ts#L1>) | pgTable learning_material_comments |
| [dozu-api-service/src/models/learningMethod.model.ts:1](<../../dozu-api-service/src/models/learningMethod.model.ts#L1>) | pgTable learning_methods |
| [dozu-api-service/src/models/llmIntegrate.model.ts:1](<../../dozu-api-service/src/models/llmIntegrate.model.ts#L1>) | pgEnum key_type, pgEnum key_status, pgTable llm_providers, pgTable llm_models, pgTable provider_llm_api_keys, pgTable llm_api_key_model |
| [dozu-api-service/src/models/mindmap/mindmap.model.ts:1](<../../dozu-api-service/src/models/mindmap/mindmap.model.ts#L1>) | pgTable mindmaps |
| [dozu-api-service/src/models/note/note.model.ts:1](<../../dozu-api-service/src/models/note/note.model.ts#L1>) | pgTable notes |
| [dozu-api-service/src/models/package/index.ts:1](<../../dozu-api-service/src/models/package/index.ts#L1>) |  |
| [dozu-api-service/src/models/package/package.model.ts:1](<../../dozu-api-service/src/models/package/package.model.ts#L1>) | pgTable packages |
| [dozu-api-service/src/models/payment/index.ts:1](<../../dozu-api-service/src/models/payment/index.ts#L1>) |  |
| [dozu-api-service/src/models/payment/transaction.model.ts:1](<../../dozu-api-service/src/models/payment/transaction.model.ts#L1>) | pgEnum payment_status, pgTable transactions |
| [dozu-api-service/src/models/progress/dailyStudy.model.ts:1](<../../dozu-api-service/src/models/progress/dailyStudy.model.ts#L1>) | pgTable daily_study_records |
| [dozu-api-service/src/models/progress/progress.model.ts:1](<../../dozu-api-service/src/models/progress/progress.model.ts#L1>) | pgEnum content_type, pgEnum progress_status, pgTable progress |
| [dozu-api-service/src/models/quiz/question.model.ts:1](<../../dozu-api-service/src/models/quiz/question.model.ts#L1>) | pgTable questions |
| [dozu-api-service/src/models/quiz/questionInQuiz.model.ts:1](<../../dozu-api-service/src/models/quiz/questionInQuiz.model.ts#L1>) | pgTable question_in_quiz |
| [dozu-api-service/src/models/quiz/questionResult.model.ts:1](<../../dozu-api-service/src/models/quiz/questionResult.model.ts#L1>) | pgTable question_result |
| [dozu-api-service/src/models/quiz/quiz.model.ts:1](<../../dozu-api-service/src/models/quiz/quiz.model.ts#L1>) | pgTable quizzes |
| [dozu-api-service/src/models/quiz/quizResult.model.ts:1](<../../dozu-api-service/src/models/quiz/quizResult.model.ts#L1>) | pgTable quiz_result |
| [dozu-api-service/src/models/schedule/reminder.model.ts:1](<../../dozu-api-service/src/models/schedule/reminder.model.ts#L1>) | pgEnum reminder_status, pgTable reminders |
| [dozu-api-service/src/models/schedule/schedule.model.ts:1](<../../dozu-api-service/src/models/schedule/schedule.model.ts#L1>) | pgTable schedules |
| [dozu-api-service/src/models/schedule/studySlot.model.ts:1](<../../dozu-api-service/src/models/schedule/studySlot.model.ts#L1>) | pgTable study_slots |
| [dozu-api-service/src/models/studySlotLearningMethod.model.ts:1](<../../dozu-api-service/src/models/studySlotLearningMethod.model.ts#L1>) | pgTable study_slots_learning_methods |
| [dozu-api-service/src/models/subscription/feature.model.ts:1](<../../dozu-api-service/src/models/subscription/feature.model.ts#L1>) | pgEnum feature_type, pgEnum feature_category, pgEnum unit, pgTable features |
| [dozu-api-service/src/models/subscription/index.ts:1](<../../dozu-api-service/src/models/subscription/index.ts#L1>) |  |
| [dozu-api-service/src/models/subscription/plan.model.ts:1](<../../dozu-api-service/src/models/subscription/plan.model.ts#L1>) | pgEnum plan_type, pgEnum billing_interval, pgTable plans |
| [dozu-api-service/src/models/subscription/planFeature.model.ts:1](<../../dozu-api-service/src/models/subscription/planFeature.model.ts#L1>) | pgEnum feature_interval, pgTable plan_features |
| [dozu-api-service/src/models/subscription/userFeatureUsage.model.ts:1](<../../dozu-api-service/src/models/subscription/userFeatureUsage.model.ts#L1>) | pgTable user_feature_usage |
| [dozu-api-service/src/models/subscription/userSubscription.model.ts:1](<../../dozu-api-service/src/models/subscription/userSubscription.model.ts#L1>) | pgEnum subscription_status, pgTable user_subscriptions |
| [dozu-api-service/src/models/teacher-request/teacherRequest.model.ts:1](<../../dozu-api-service/src/models/teacher-request/teacherRequest.model.ts#L1>) | pgEnum teacher_request_status, pgTable teacher_requests |
| [dozu-api-service/src/models/topic/topic.model.ts:1](<../../dozu-api-service/src/models/topic/topic.model.ts#L1>) | pgTable topics |
| [dozu-api-service/src/models/topic/userTopicSetting.model.ts:1](<../../dozu-api-service/src/models/topic/userTopicSetting.model.ts#L1>) | pgTable user_topic_settings |
| [dozu-api-service/src/models/tracking/itemSpacedRepetitionTracking.model.ts:1](<../../dozu-api-service/src/models/tracking/itemSpacedRepetitionTracking.model.ts#L1>) | pgEnum item_status_type, pgEnum item_type_type, pgTable item_spaced_repetition_tracking |
| [dozu-api-service/src/models/tracking/taskProgress.model.ts:1](<../../dozu-api-service/src/models/tracking/taskProgress.model.ts#L1>) | pgTable task_progress |
| [dozu-api-service/src/models/user.model.ts:1](<../../dozu-api-service/src/models/user.model.ts#L1>) | pgEnum role, pgTable users |

## Migration provenance

All 20 SQL migrations, their 20 journal entries and snapshot JSON files exist locally but are ignored by `drizzle/` and are absent from the source commit. A clean Git import loses them. Hashes preserve this local evidence without claiming an approved migration history.

| Local migration | Tracked | SHA-256 |
| --- | --- | --- |
| [dozu-api-service/drizzle/0000_ambiguous_white_tiger.sql:1](<../../dozu-api-service/drizzle/0000_ambiguous_white_tiger.sql#L1>) | **NO — ignored local artifact** | cb4a2767f39c247f1aae9cee74ebbc84a4c662b9491f14014c4e34519a902efb |
| [dozu-api-service/drizzle/0001_orange_joshua_kane.sql:1](<../../dozu-api-service/drizzle/0001_orange_joshua_kane.sql#L1>) | **NO — ignored local artifact** | 33a69a9487343c7a5462d2c2ad78573eeab61e959bbbf95606c4313999abf4b0 |
| [dozu-api-service/drizzle/0002_feature_usage_period_unique.sql:1](<../../dozu-api-service/drizzle/0002_feature_usage_period_unique.sql#L1>) | **NO — ignored local artifact** | 636e7d858e99733ce417729e2b513a2ae87d952b9a0393d6cf567a7969d32293 |
| [dozu-api-service/drizzle/0002_tiresome_rockslide.sql:1](<../../dozu-api-service/drizzle/0002_tiresome_rockslide.sql#L1>) | **NO — ignored local artifact** | 022994a1a69d7bcb6fe72a85ad1da577c2d802285c9c1005ceffe9c9b90183a5 |
| [dozu-api-service/drizzle/0003_wealthy_hellcat.sql:1](<../../dozu-api-service/drizzle/0003_wealthy_hellcat.sql#L1>) | **NO — ignored local artifact** | 0262ed06c8621f4c0401c39e6bd2486e788f6f3c20f8ec14eb255e4a6e7a7062 |
| [dozu-api-service/drizzle/0004_clean_human_fly.sql:1](<../../dozu-api-service/drizzle/0004_clean_human_fly.sql#L1>) | **NO — ignored local artifact** | 85691b918f5981c742f473761a1ad6dc01b2bca0e24df8189081fc85da2b5863 |
| [dozu-api-service/drizzle/0005_acoustic_the_phantom.sql:1](<../../dozu-api-service/drizzle/0005_acoustic_the_phantom.sql#L1>) | **NO — ignored local artifact** | 074d6c238cb16ac4a5ebc1b686833255fe9ef054ce55951494e5881b6a460f71 |
| [dozu-api-service/drizzle/0007_superb_quasimodo.sql:1](<../../dozu-api-service/drizzle/0007_superb_quasimodo.sql#L1>) | **NO — ignored local artifact** | 37fad5193e4113d7fe310af855b0feeed55c83850868dddfdd89aa379ecc12be |
| [dozu-api-service/drizzle/0008_remarkable_invaders.sql:1](<../../dozu-api-service/drizzle/0008_remarkable_invaders.sql#L1>) | **NO — ignored local artifact** | dbf4af083da155adc486451ea0bf9ad973c734dddaed43b3523fda08a1ec13a0 |
| [dozu-api-service/drizzle/0009_pale_changeling.sql:1](<../../dozu-api-service/drizzle/0009_pale_changeling.sql#L1>) | **NO — ignored local artifact** | 22083ee0d3147735870383a66659851af4d00b6971f94a38ab1b59199ba0fb59 |
| [dozu-api-service/drizzle/0010_sudden_lady_mastermind.sql:1](<../../dozu-api-service/drizzle/0010_sudden_lady_mastermind.sql#L1>) | **NO — ignored local artifact** | 111e7d3d02046dfe9f78887931df9f14fcfa13c9d2191298c4463a7d5227f44f |
| [dozu-api-service/drizzle/0011_amused_betty_brant.sql:1](<../../dozu-api-service/drizzle/0011_amused_betty_brant.sql#L1>) | **NO — ignored local artifact** | 123c6bd007ddb520cd74f2ccdb7350e4a13abe1185687016700971cdf437dd8f |
| [dozu-api-service/drizzle/0012_rainy_slayback.sql:1](<../../dozu-api-service/drizzle/0012_rainy_slayback.sql#L1>) | **NO — ignored local artifact** | 212cc5c8ac54be48ef23ce3b689c0d9642e3856c5792aa05dd2d4dfafaac99eb |
| [dozu-api-service/drizzle/0013_numerous_big_bertha.sql:1](<../../dozu-api-service/drizzle/0013_numerous_big_bertha.sql#L1>) | **NO — ignored local artifact** | c991b11e96543e4f89dbf7e4b32190cc267a9f4dbb98350fa3e2e003a7722162 |
| [dozu-api-service/drizzle/0014_warm_lord_tyger.sql:1](<../../dozu-api-service/drizzle/0014_warm_lord_tyger.sql#L1>) | **NO — ignored local artifact** | 3a6d49ed8fa57a0c01fddbd65fdfa4e41cdace6eb3b16190f3822b964cd739c1 |
| [dozu-api-service/drizzle/0015_acoustic_hellcat.sql:1](<../../dozu-api-service/drizzle/0015_acoustic_hellcat.sql#L1>) | **NO — ignored local artifact** | 7073a679bb404eae642920b7873295f5ebd179083210db0c24d4131d629e905b |
| [dozu-api-service/drizzle/0016_flaky_mandarin.sql:1](<../../dozu-api-service/drizzle/0016_flaky_mandarin.sql#L1>) | **NO — ignored local artifact** | 19f107b9d40d2d6b32391d13355b23e9d7852672e813a193d5683b63100e5e61 |
| [dozu-api-service/drizzle/0017_glossy_roland_deschain.sql:1](<../../dozu-api-service/drizzle/0017_glossy_roland_deschain.sql#L1>) | **NO — ignored local artifact** | 1ebfc3e42a1909c5446110487d772d3ba2f809afef1bd47146dc8001188f748d |
| [dozu-api-service/drizzle/0018_unknown_mongu.sql:1](<../../dozu-api-service/drizzle/0018_unknown_mongu.sql#L1>) | **NO — ignored local artifact** | 9554c3d4b3d877af48da965e97f484e0ddd7c3129e7766e657cef4874dac86e4 |
| [dozu-api-service/drizzle/0019_sparkling_lethal_legion.sql:1](<../../dozu-api-service/drizzle/0019_sparkling_lethal_legion.sql#L1>) | **NO — ignored local artifact** | 3d710a0fb261555740acaaa6b20bca5a9c1726a4a241f104b98257a866ea4ceb |

Runtime uses DATABASE_URL through pg/Drizzle; Drizzle tooling separately uses DATABASE_URL_DRIZZLE_MIGRATE and different dotenv selection. Bootstrap must reconcile these profiles, explicitly create pgvector before vector tables, apply reviewed migrations and seed roles/permissions/plans/features/LLM metadata without embedded keys. No migration was applied and no database/dump/user records were read.

PostgreSQL-specific dependencies: enums, serial sequences, FK/cascade/unique constraints, timestamps/time zones, arrays/JSONB, `ILIKE`, PostgreSQL SQL fragments, `vector(384)` and HNSW cosine operators. [dozu-api-service/src/models/embedding/embedding.model.ts:21](<../../dozu-api-service/src/models/embedding/embedding.model.ts#L21>) and [dozu-api-service/src/repositories/embedding/embedding.repo.ts:113](<../../dozu-api-service/src/repositories/embedding/embedding.repo.ts#L113>) anchor the vector contract. Local SQL migration 0013 creates vector/HNSW but the collected SQL has no CREATE EXTENSION statement. The container profiles reference PostgreSQL 16/17 without proving extension installation.

`scripts/populate-test-data.ts` is a developer test-data script, not a clean-machine first-boot seed contract. Verify model/migration drift with a new disposable local cluster under #29/#40, including upgrades/rollback backup, missing FK data and unique-index behavior. SQLite is not a proven drop-in replacement.
