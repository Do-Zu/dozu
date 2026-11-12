CREATE TYPE "public"."role" AS ENUM('user', 'admin');--> statement-breakpoint
CREATE TYPE "public"."key_status" AS ENUM('active', 'inactive', 'expired', 'rate_limited');--> statement-breakpoint
CREATE TYPE "public"."key_type" AS ENUM('free', 'paid');--> statement-breakpoint
CREATE TYPE "public"."item_status_type" AS ENUM('new', 'learning', 'review');--> statement-breakpoint
CREATE TYPE "public"."item_type_type" AS ENUM('flashcard', 'question');--> statement-breakpoint
CREATE TYPE "public"."reminder_status" AS ENUM('pending', 'accepted', 'declined');--> statement-breakpoint
CREATE TYPE "public"."billing_interval" AS ENUM('monthly', 'yearly', 'custom');--> statement-breakpoint
CREATE TYPE "public"."plan_type" AS ENUM('free', 'pro', 'team', 'enterprise');--> statement-breakpoint
CREATE TYPE "public"."feature_category" AS ENUM('core', 'storage', 'integrations', 'customization');--> statement-breakpoint
CREATE TYPE "public"."feature_type" AS ENUM('boolean', 'usage', 'size_limit');--> statement-breakpoint
CREATE TYPE "public"."unit" AS ENUM('GB', 'MB', 'count');--> statement-breakpoint
CREATE TYPE "public"."feature_interval" AS ENUM('daily', 'weekly', 'monthly', 'yearly', 'lifetime');--> statement-breakpoint
CREATE TYPE "public"."payment_status" AS ENUM('pending', 'processing', 'success', 'failed', 'expired', 'cancelled');--> statement-breakpoint
CREATE TYPE "public"."subscription_status" AS ENUM('active', 'cancelled', 'expired', 'pending', 'suspended', 'trialing');--> statement-breakpoint
CREATE TYPE "public"."node_type" AS ENUM('mindmap', 'flashcard', 'quiz');--> statement-breakpoint
CREATE TYPE "public"."teacher_request_status" AS ENUM('pending', 'approved', 'rejected');--> statement-breakpoint
CREATE TABLE "demo" (
	"id" integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY (sequence name "demo_id_seq" INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START WITH 1 CACHE 1),
	"action" varchar(255) NOT NULL,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "flashcards" (
	"flashcard_id" serial PRIMARY KEY NOT NULL,
	"topic_id" integer NOT NULL,
	"node_id" text,
	"front" text NOT NULL,
	"back" text NOT NULL,
	"image_url" text,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "users" (
	"user_id" serial PRIMARY KEY NOT NULL,
	"username" varchar(50) NOT NULL,
	"email" varchar(100) NOT NULL,
	"password_hash" text,
	"full_name" varchar(100),
	"avatar_url" text DEFAULT 'https://res.cloudinary.com/dsvllb1am/image/upload/f_auto,q_auto/v1/default/tcd6nnm6lgn0jb3puton' NOT NULL,
	"role" "role" DEFAULT 'user' NOT NULL,
	"display_name" varchar(100),
	"bio" text,
	"location" varchar(100),
	"website" varchar(255),
	"hobbies_topic" text,
	"learning_goals" jsonb,
	"study_preferences" jsonb,
	"difficulty_level" varchar(20) DEFAULT 'beginner',
	"notification_settings" jsonb DEFAULT '{"dailyReminders":true,"weeklyReports":true,"achievementNotifications":true,"emailNotifications":true,"pushNotifications":true}'::jsonb,
	"privacy_settings" jsonb DEFAULT '{"showProfile":true,"showProgress":true,"showAchievements":true,"allowMessages":true}'::jsonb,
	"is_public" boolean DEFAULT true,
	"is_complete" boolean DEFAULT false,
	"preferences" jsonb,
	"free_time" jsonb,
	"busy_time" jsonb,
	"avg_study_duration" interval,
	"is_active" boolean DEFAULT true,
	"is_verified" boolean DEFAULT false,
	"is_new_user" boolean DEFAULT true,
	"has_completed_onboarding" boolean DEFAULT false,
	"created_at" timestamp with time zone DEFAULT now(),
	"updated_at" timestamp with time zone,
	"last_login_at" timestamp with time zone,
	"last_active_at" timestamp with time zone,
	CONSTRAINT "users_username_unique" UNIQUE("username"),
	CONSTRAINT "users_email_unique" UNIQUE("email")
);
--> statement-breakpoint
CREATE TABLE "topics" (
	"topic_id" serial PRIMARY KEY NOT NULL,
	"class_id" integer,
	"user_id" integer NOT NULL,
	"name" varchar(255) NOT NULL,
	"description" text DEFAULT '' NOT NULL,
	"image_url" text,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "input_set" (
	"set_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"topic_id" integer,
	"title" varchar(255) NOT NULL,
	"description" varchar(255),
	"content_type" varchar(50),
	"metadata" jsonb,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "llm_api_key_model" (
	"id" serial PRIMARY KEY NOT NULL,
	"api_key_id" integer NOT NULL,
	"model_id" integer NOT NULL,
	"request_per_minute" integer NOT NULL,
	"request_per_day" integer NOT NULL,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "llm_models" (
	"id" serial PRIMARY KEY NOT NULL,
	"provider_id" integer NOT NULL,
	"name" varchar(100) NOT NULL,
	"priority" integer DEFAULT 0 NOT NULL,
	"is_available" boolean DEFAULT true NOT NULL,
	"is_default" boolean DEFAULT false NOT NULL,
	"description" text,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "llm_providers" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" varchar(100) NOT NULL,
	"is_default" boolean DEFAULT false NOT NULL,
	"is_available" boolean DEFAULT true NOT NULL,
	"index" integer NOT NULL,
	"description" text,
	"base_url" text,
	"created_at" timestamp with time zone DEFAULT now(),
	CONSTRAINT "llm_providers_name_unique" UNIQUE("name")
);
--> statement-breakpoint
CREATE TABLE "provider_llm_api_keys" (
	"id" serial PRIMARY KEY NOT NULL,
	"provider_id" integer NOT NULL,
	"is_default" boolean DEFAULT false NOT NULL,
	"priority" integer DEFAULT 0 NOT NULL,
	"index" integer NOT NULL,
	"key_value" text NOT NULL,
	"key_type" "key_type" NOT NULL,
	"status" "key_status" DEFAULT 'active' NOT NULL,
	"usage_limit_per_day" integer,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "questions" (
	"question_id" serial PRIMARY KEY NOT NULL,
	"topic_id" integer NOT NULL,
	"question_text" text DEFAULT '' NOT NULL,
	"choices" text[],
	"correct_index" integer,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "quizzes" (
	"quiz_id" serial PRIMARY KEY NOT NULL,
	"topic_id" integer NOT NULL,
	"name" text,
	"description" text
);
--> statement-breakpoint
CREATE TABLE "question_in_quiz" (
	"quiz_id" integer NOT NULL,
	"question_id" integer NOT NULL,
	CONSTRAINT "question_in_quiz_quiz_id_question_id_pk" PRIMARY KEY("quiz_id","question_id")
);
--> statement-breakpoint
CREATE TABLE "quiz_result" (
	"quiz_result_id" serial PRIMARY KEY NOT NULL,
	"quiz_id" integer NOT NULL,
	"user_id" integer NOT NULL,
	"correct_answers_count" integer,
	"questions_count" integer,
	"time_reviewed" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "item_spaced_repetition_tracking" (
	"item_id" integer NOT NULL,
	"user_id" integer NOT NULL,
	"topic_id" integer NOT NULL,
	"type" "item_type_type" NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"repetition_number" integer DEFAULT 0 NOT NULL,
	"easiness_factor" numeric(3, 2) DEFAULT '2.5' NOT NULL,
	"review_interval" integer DEFAULT 0 NOT NULL,
	"last_reviewed" date,
	"next_review" date DEFAULT now() NOT NULL,
	"status" "item_status_type" DEFAULT 'new' NOT NULL,
	CONSTRAINT "item_spaced_repetition_tracking_item_id_user_id_type_pk" PRIMARY KEY("item_id","user_id","type")
);
--> statement-breakpoint
CREATE TABLE "schedules" (
	"id" serial PRIMARY KEY NOT NULL,
	"topic_id" integer NOT NULL,
	"start_time" timestamp with time zone NOT NULL,
	"end_time" timestamp with time zone NOT NULL,
	"percent_complete" double precision DEFAULT 0,
	"completed" boolean DEFAULT false,
	"rescheduled" boolean DEFAULT false
);
--> statement-breakpoint
CREATE TABLE "study_slots" (
	"study_slot_id" serial PRIMARY KEY NOT NULL,
	"topic_id" integer NOT NULL,
	"title" varchar(255) NOT NULL,
	"estimated_time" interval,
	"priority" integer,
	"start_time" timestamp with time zone NOT NULL,
	"end_time" timestamp with time zone NOT NULL,
	"percent_complete" real DEFAULT 0,
	"is_completed" boolean DEFAULT false,
	"deadline" timestamp with time zone,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "learning_methods" (
	"id" serial PRIMARY KEY NOT NULL,
	"user_id" integer,
	"name" varchar(255) NOT NULL,
	"description" text,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "study_slots_learning_methods" (
	"id" serial PRIMARY KEY NOT NULL,
	"task_id" integer NOT NULL,
	"method_id" integer NOT NULL,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "reminders" (
	"id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"task_id" integer NOT NULL,
	"original_schedule_id" integer,
	"new_schedule_id" integer,
	"new_suggested_time" timestamp with time zone NOT NULL,
	"overdue" boolean DEFAULT false,
	"status" "reminder_status" DEFAULT 'pending',
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "task_progress" (
	"progress_id" serial PRIMARY KEY NOT NULL,
	"task_id" integer NOT NULL,
	"percent_complete" double precision,
	"completed" boolean DEFAULT false,
	"updated_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "mindmaps" (
	"mindmap_id" serial PRIMARY KEY NOT NULL,
	"topic_id" integer NOT NULL,
	"title" varchar(255) DEFAULT 'New mind map',
	"mindmap_data" jsonb,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "email_verification_codes" (
	"email_verification_code_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"verification_code" text,
	"expiration" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "auth_accounts" (
	"auth_account_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"provider" text NOT NULL,
	"provider_id" text NOT NULL,
	"created_at" timestamp DEFAULT now(),
	CONSTRAINT "auth_accounts_provider_provider_id_unique" UNIQUE("provider","provider_id")
);
--> statement-breakpoint
CREATE TABLE "roles" (
	"role_id" serial PRIMARY KEY NOT NULL,
	"name" varchar(64) NOT NULL,
	"description" text NOT NULL
);
--> statement-breakpoint
CREATE TABLE "user_roles" (
	"user_id" integer NOT NULL,
	"role_id" integer NOT NULL,
	CONSTRAINT "user_roles_user_id_role_id_unique" UNIQUE("user_id","role_id")
);
--> statement-breakpoint
CREATE TABLE "permissions" (
	"permission_id" serial PRIMARY KEY NOT NULL,
	"name" varchar(128) NOT NULL,
	"description" text NOT NULL
);
--> statement-breakpoint
CREATE TABLE "role_permissions" (
	"role_id" integer NOT NULL,
	"permission_id" integer NOT NULL,
	CONSTRAINT "role_permissions_role_id_permission_id_unique" UNIQUE("role_id","permission_id")
);
--> statement-breakpoint
CREATE TABLE "plans" (
	"plan_id" serial PRIMARY KEY NOT NULL,
	"name" varchar(100) NOT NULL,
	"description" text,
	"plan_type" "plan_type" NOT NULL,
	"billing_interval" "billing_interval" NOT NULL,
	"price" numeric(10, 2) NOT NULL,
	"currency" varchar(3) DEFAULT 'USD' NOT NULL,
	"is_active" boolean DEFAULT true NOT NULL,
	"created_at" timestamp with time zone DEFAULT now(),
	"updated_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "features" (
	"feature_id" serial PRIMARY KEY NOT NULL,
	"name" varchar(100) NOT NULL,
	"description" text,
	"feature_type" "feature_type" NOT NULL,
	"category" "feature_category" NOT NULL,
	"unit" "unit",
	"is_active" boolean DEFAULT true NOT NULL,
	"sort_order" integer DEFAULT 0 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now(),
	"updated_at" timestamp with time zone,
	CONSTRAINT "features_name_unique" UNIQUE("name")
);
--> statement-breakpoint
CREATE TABLE "plan_features" (
	"plan_feature_id" serial PRIMARY KEY NOT NULL,
	"plan_id" integer NOT NULL,
	"feature_id" integer NOT NULL,
	"boolean_value" boolean,
	"numeric_value" numeric(15, 2),
	"text_value" text,
	"interval" "feature_interval" DEFAULT 'daily' NOT NULL,
	"api_url" varchar(255) NOT NULL,
	"is_unlimited" boolean DEFAULT false NOT NULL,
	"is_enabled" boolean DEFAULT true NOT NULL,
	"created_at" timestamp with time zone DEFAULT now(),
	"updated_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "user_subscriptions" (
	"subscription_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"plan_id" integer NOT NULL,
	"status" "subscription_status" DEFAULT 'pending' NOT NULL,
	"current_period_start" timestamp with time zone NOT NULL,
	"current_period_end" timestamp with time zone NOT NULL,
	"trial_start" timestamp with time zone,
	"trial_end" timestamp with time zone,
	"cancel_at" timestamp with time zone,
	"canceled_at" timestamp with time zone,
	"cancellation_reason" text,
	"external_subscription_id" varchar(255),
	"auto_renew" boolean DEFAULT true NOT NULL,
	"created_at" timestamp with time zone DEFAULT now(),
	"updated_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "user_feature_usage" (
	"usage_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"feature_id" integer NOT NULL,
	"subscription_id" integer,
	"used_value" numeric(15, 2) DEFAULT '0' NOT NULL,
	"limit_value" numeric(15, 2),
	"is_unlimited" boolean DEFAULT false NOT NULL,
	"reset_period_start" timestamp with time zone NOT NULL,
	"reset_period_end" timestamp with time zone NOT NULL,
	"last_reset_at" timestamp with time zone,
	"created_at" timestamp with time zone DEFAULT now(),
	"updated_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "transactions" (
	"transaction_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"gateway" varchar(100) NOT NULL,
	"transaction_date" timestamp DEFAULT now() NOT NULL,
	"account_number" varchar(100),
	"amount" numeric(20, 2) DEFAULT '0.00' NOT NULL,
	"currency" varchar(5) NOT NULL,
	"code" varchar(250),
	"payment_id" varchar(250),
	"desc" text,
	"status" "payment_status" DEFAULT 'pending' NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone,
	"metadata" json
);
--> statement-breakpoint
CREATE TABLE "classes" (
	"class_id" serial PRIMARY KEY NOT NULL,
	"teacher_id" integer NOT NULL,
	"name" varchar(255) NOT NULL,
	"description" text DEFAULT '' NOT NULL,
	"invitation_code" varchar(10) NOT NULL,
	"image_url" text,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	CONSTRAINT "classes_invitation_code_unique" UNIQUE("invitation_code")
);
--> statement-breakpoint
CREATE TABLE "class_enrollments" (
	"class_enrollment_id" serial PRIMARY KEY NOT NULL,
	"class_id" integer NOT NULL,
	"student_id" integer NOT NULL,
	"enrolled_at" timestamp with time zone DEFAULT now() NOT NULL,
	CONSTRAINT "class_enrollments_class_id_student_id_unique" UNIQUE("class_id","student_id")
);
--> statement-breakpoint
CREATE TABLE "class_topic_comments" (
	"comment_id" serial PRIMARY KEY NOT NULL,
	"topic_id" integer NOT NULL,
	"node_id" varchar(36) NOT NULL,
	"author" jsonb NOT NULL,
	"node_type" "node_type" NOT NULL,
	"is_deleted" boolean DEFAULT false NOT NULL,
	"parent_cmt_id" integer,
	"level" integer DEFAULT 0 NOT NULL,
	"content" text NOT NULL,
	"reaction_count" integer DEFAULT 0 NOT NULL,
	"reply_count" integer DEFAULT 0 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "teacher_requests" (
	"request_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"description" text DEFAULT '' NOT NULL,
	"status" "teacher_request_status" DEFAULT 'pending' NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
ALTER TABLE "flashcards" ADD CONSTRAINT "flashcards_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "topics" ADD CONSTRAINT "topics_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "topics" ADD CONSTRAINT "topics_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "input_set" ADD CONSTRAINT "input_set_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "input_set" ADD CONSTRAINT "input_set_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "llm_api_key_model" ADD CONSTRAINT "llm_api_key_model_api_key_id_provider_llm_api_keys_id_fk" FOREIGN KEY ("api_key_id") REFERENCES "public"."provider_llm_api_keys"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "llm_api_key_model" ADD CONSTRAINT "llm_api_key_model_model_id_llm_models_id_fk" FOREIGN KEY ("model_id") REFERENCES "public"."llm_models"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "llm_models" ADD CONSTRAINT "llm_models_provider_id_llm_providers_id_fk" FOREIGN KEY ("provider_id") REFERENCES "public"."llm_providers"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "provider_llm_api_keys" ADD CONSTRAINT "provider_llm_api_keys_provider_id_llm_providers_id_fk" FOREIGN KEY ("provider_id") REFERENCES "public"."llm_providers"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "questions" ADD CONSTRAINT "questions_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "quizzes" ADD CONSTRAINT "quizzes_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "question_in_quiz" ADD CONSTRAINT "question_in_quiz_quiz_id_quizzes_quiz_id_fk" FOREIGN KEY ("quiz_id") REFERENCES "public"."quizzes"("quiz_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "question_in_quiz" ADD CONSTRAINT "question_in_quiz_question_id_questions_question_id_fk" FOREIGN KEY ("question_id") REFERENCES "public"."questions"("question_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "quiz_result" ADD CONSTRAINT "quiz_result_quiz_id_quizzes_quiz_id_fk" FOREIGN KEY ("quiz_id") REFERENCES "public"."quizzes"("quiz_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "quiz_result" ADD CONSTRAINT "quiz_result_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "item_spaced_repetition_tracking" ADD CONSTRAINT "item_spaced_repetition_tracking_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "item_spaced_repetition_tracking" ADD CONSTRAINT "item_spaced_repetition_tracking_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "schedules" ADD CONSTRAINT "schedules_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "study_slots" ADD CONSTRAINT "study_slots_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "learning_methods" ADD CONSTRAINT "learning_methods_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE set null ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "study_slots_learning_methods" ADD CONSTRAINT "study_slots_learning_methods_task_id_study_slots_study_slot_id_fk" FOREIGN KEY ("task_id") REFERENCES "public"."study_slots"("study_slot_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "study_slots_learning_methods" ADD CONSTRAINT "study_slots_learning_methods_method_id_learning_methods_id_fk" FOREIGN KEY ("method_id") REFERENCES "public"."learning_methods"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "reminders" ADD CONSTRAINT "reminders_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "reminders" ADD CONSTRAINT "reminders_task_id_study_slots_study_slot_id_fk" FOREIGN KEY ("task_id") REFERENCES "public"."study_slots"("study_slot_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "reminders" ADD CONSTRAINT "reminders_original_schedule_id_schedules_id_fk" FOREIGN KEY ("original_schedule_id") REFERENCES "public"."schedules"("id") ON DELETE set null ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "reminders" ADD CONSTRAINT "reminders_new_schedule_id_schedules_id_fk" FOREIGN KEY ("new_schedule_id") REFERENCES "public"."schedules"("id") ON DELETE set null ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "task_progress" ADD CONSTRAINT "task_progress_task_id_study_slots_study_slot_id_fk" FOREIGN KEY ("task_id") REFERENCES "public"."study_slots"("study_slot_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "mindmaps" ADD CONSTRAINT "mindmaps_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "email_verification_codes" ADD CONSTRAINT "email_verification_codes_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "auth_accounts" ADD CONSTRAINT "auth_accounts_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_roles" ADD CONSTRAINT "user_roles_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_roles" ADD CONSTRAINT "user_roles_role_id_roles_role_id_fk" FOREIGN KEY ("role_id") REFERENCES "public"."roles"("role_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "role_permissions" ADD CONSTRAINT "role_permissions_role_id_roles_role_id_fk" FOREIGN KEY ("role_id") REFERENCES "public"."roles"("role_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "role_permissions" ADD CONSTRAINT "role_permissions_permission_id_permissions_permission_id_fk" FOREIGN KEY ("permission_id") REFERENCES "public"."permissions"("permission_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "plan_features" ADD CONSTRAINT "plan_features_plan_id_fk" FOREIGN KEY ("plan_id") REFERENCES "public"."plans"("plan_id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "plan_features" ADD CONSTRAINT "plan_features_feature_id_fk" FOREIGN KEY ("feature_id") REFERENCES "public"."features"("feature_id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_subscriptions" ADD CONSTRAINT "user_subscriptions_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_subscriptions" ADD CONSTRAINT "user_subscriptions_plan_id_fk" FOREIGN KEY ("plan_id") REFERENCES "public"."plans"("plan_id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_feature_usage" ADD CONSTRAINT "user_feature_usage_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_feature_usage" ADD CONSTRAINT "user_feature_usage_feature_id_features_feature_id_fk" FOREIGN KEY ("feature_id") REFERENCES "public"."features"("feature_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_feature_usage" ADD CONSTRAINT "user_feature_usage_subscription_id_user_subscriptions_subscription_id_fk" FOREIGN KEY ("subscription_id") REFERENCES "public"."user_subscriptions"("subscription_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_feature_usage" ADD CONSTRAINT "user_feature_usage_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_feature_usage" ADD CONSTRAINT "user_feature_usage_feature_id_fk" FOREIGN KEY ("feature_id") REFERENCES "public"."features"("feature_id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_feature_usage" ADD CONSTRAINT "user_feature_usage_subscription_id_fk" FOREIGN KEY ("subscription_id") REFERENCES "public"."user_subscriptions"("subscription_id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "transactions" ADD CONSTRAINT "transactions_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "classes" ADD CONSTRAINT "classes_teacher_id_users_user_id_fk" FOREIGN KEY ("teacher_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_enrollments" ADD CONSTRAINT "class_enrollments_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_enrollments" ADD CONSTRAINT "class_enrollments_student_id_users_user_id_fk" FOREIGN KEY ("student_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_topic_comments" ADD CONSTRAINT "class_topic_comments_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_topic_comments" ADD CONSTRAINT "class_topic_comments_parent_cmt_id_class_topic_comments_comment_id_fk" FOREIGN KEY ("parent_cmt_id") REFERENCES "public"."class_topic_comments"("comment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "teacher_requests" ADD CONSTRAINT "teacher_requests_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE UNIQUE INDEX "api_key_model_unique" ON "llm_api_key_model" USING btree ("api_key_id","model_id");--> statement-breakpoint
CREATE UNIQUE INDEX "provider_model_unique" ON "llm_models" USING btree ("provider_id","name");--> statement-breakpoint
CREATE UNIQUE INDEX "unique_plan_type_interval" ON "plans" USING btree ("plan_type","billing_interval");--> statement-breakpoint
CREATE UNIQUE INDEX "unique_plan_feature" ON "plan_features" USING btree ("plan_id","feature_id");