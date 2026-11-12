CREATE TYPE "public"."backlog_source" AS ENUM('first_half', 'second_half', 'manual', 'backlog_quiz');--> statement-breakpoint
CREATE TYPE "public"."backlog_status" AS ENUM('active', 'reserved', 'consumed');--> statement-breakpoint
CREATE TABLE "flashcard_backlog_items" (
	"id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"topic_id" integer NOT NULL,
	"flashcard_id" integer NOT NULL,
	"source" "backlog_source" NOT NULL,
	"status" "backlog_status" DEFAULT 'active' NOT NULL,
	"session_epoch" integer,
	"order_index" integer,
	"client_request_id" varchar(64),
	"created_at" timestamp with time zone DEFAULT now(),
	"reserved_at" timestamp with time zone,
	"consumed_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "point_transactions" (
	"transaction_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"points" integer NOT NULL,
	"type" varchar(50) NOT NULL,
	"description" text,
	"related_id" integer,
	"related_type" varchar(50),
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "points" (
	"points_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"total_points" integer DEFAULT 0 NOT NULL,
	"available_points" integer DEFAULT 0 NOT NULL,
	"lifetime_points" integer DEFAULT 0 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now(),
	"updated_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "achievements" (
	"achievement_id" serial PRIMARY KEY NOT NULL,
	"name" varchar(100) NOT NULL,
	"description" text NOT NULL,
	"icon" varchar(255),
	"points" integer DEFAULT 0 NOT NULL,
	"type" varchar(50) NOT NULL,
	"condition" text NOT NULL,
	"is_active" boolean DEFAULT true NOT NULL,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "user_achievements" (
	"user_achievement_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"achievement_id" integer NOT NULL,
	"earned_at" timestamp with time zone DEFAULT now(),
	"progress" integer DEFAULT 0 NOT NULL
);
--> statement-breakpoint
CREATE TABLE "anki_settings" (
	"anki_setting_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"is_default" boolean DEFAULT false NOT NULL,
	"learning_steps" integer[] DEFAULT '{1,10}' NOT NULL,
	"graduating_interval" integer DEFAULT 1 NOT NULL,
	"easy_interval" integer DEFAULT 4 NOT NULL,
	"relearning_steps" integer[] DEFAULT '{10}' NOT NULL,
	"minimum_interval" integer DEFAULT 1 NOT NULL,
	"maximum_interval" integer DEFAULT 36500 NOT NULL,
	"starting_ease" real DEFAULT 2.5 NOT NULL,
	"easy_bonus" real DEFAULT 1.3 NOT NULL,
	"interval_modifier" real DEFAULT 1 NOT NULL,
	"hard_interval" real DEFAULT 1.2 NOT NULL,
	"new_interval" real DEFAULT 0 NOT NULL,
	"new_cards_per_day" integer DEFAULT 20 NOT NULL,
	"maximum_reviews_per_day" integer DEFAULT 200 NOT NULL,
	CONSTRAINT "graduating_interval_bounds" CHECK ("anki_settings"."graduating_interval" BETWEEN 1 AND 9999),
	CONSTRAINT "easy_interval_bounds" CHECK ("anki_settings"."easy_interval" BETWEEN 1 AND 9999),
	CONSTRAINT "minimum_interval_bounds" CHECK ("anki_settings"."minimum_interval" BETWEEN 1 AND 9999),
	CONSTRAINT "maximum_interval_bounds" CHECK ("anki_settings"."maximum_interval" BETWEEN 1 AND 36500),
	CONSTRAINT "starting_ease_bounds" CHECK ("anki_settings"."starting_ease" > 1.3 AND "anki_settings"."starting_ease" <= 5),
	CONSTRAINT "easy_bonus_bounds" CHECK ("anki_settings"."easy_bonus" BETWEEN 1 AND 5),
	CONSTRAINT "interval_modifier_bounds" CHECK ("anki_settings"."interval_modifier" BETWEEN 0.5 AND 2),
	CONSTRAINT "hard_interval_bounds" CHECK ("anki_settings"."hard_interval" BETWEEN 0.5 AND 1.3),
	CONSTRAINT "new_interval_bounds" CHECK ("anki_settings"."new_interval" BETWEEN 0 AND 1),
	CONSTRAINT "new_cards_per_day_bounds" CHECK ("anki_settings"."new_cards_per_day" BETWEEN 0 AND 9999),
	CONSTRAINT "maximum_reviews_per_day_bounds" CHECK ("anki_settings"."maximum_reviews_per_day" BETWEEN 0 AND 9999),
	CONSTRAINT "interval_range_valid" CHECK ("anki_settings"."maximum_interval" >= "anki_settings"."minimum_interval")
);
--> statement-breakpoint
CREATE TABLE "user_topic_settings" (
	"user_topic_setting_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"topic_id" integer NOT NULL,
	"setting_id" integer NOT NULL
);
--> statement-breakpoint
ALTER TABLE "users" ADD COLUMN "current_streak" integer DEFAULT 0 NOT NULL;--> statement-breakpoint
ALTER TABLE "users" ADD COLUMN "longest_streak" integer DEFAULT 0 NOT NULL;--> statement-breakpoint
ALTER TABLE "users" ADD COLUMN "last_study_date" timestamp with time zone DEFAULT now();--> statement-breakpoint
ALTER TABLE "users" ADD COLUMN "streak_freeze_used" boolean DEFAULT false;--> statement-breakpoint
ALTER TABLE "users" ADD COLUMN "streak_freeze_count" integer DEFAULT 0 NOT NULL;--> statement-breakpoint
ALTER TABLE "flashcard_backlog_items" ADD CONSTRAINT "flashcard_backlog_items_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "flashcard_backlog_items" ADD CONSTRAINT "flashcard_backlog_items_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "flashcard_backlog_items" ADD CONSTRAINT "flashcard_backlog_items_flashcard_id_flashcards_flashcard_id_fk" FOREIGN KEY ("flashcard_id") REFERENCES "public"."flashcards"("flashcard_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "point_transactions" ADD CONSTRAINT "point_transactions_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "points" ADD CONSTRAINT "points_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_achievements" ADD CONSTRAINT "user_achievements_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_achievements" ADD CONSTRAINT "user_achievements_achievement_id_achievements_achievement_id_fk" FOREIGN KEY ("achievement_id") REFERENCES "public"."achievements"("achievement_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "anki_settings" ADD CONSTRAINT "anki_settings_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_topic_settings" ADD CONSTRAINT "user_topic_settings_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_topic_settings" ADD CONSTRAINT "user_topic_settings_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_topic_settings" ADD CONSTRAINT "user_topic_settings_setting_id_anki_settings_anki_setting_id_fk" FOREIGN KEY ("setting_id") REFERENCES "public"."anki_settings"("anki_setting_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_topic_settings" ADD CONSTRAINT "user_topic_settings_setting_id_user_id_anki_settings_anki_setting_id_user_id_fk" FOREIGN KEY ("setting_id","user_id") REFERENCES "public"."anki_settings"("anki_setting_id","user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE UNIQUE INDEX "uq_backlog_user_topic_flashcard" ON "flashcard_backlog_items" USING btree ("user_id","topic_id","flashcard_id");--> statement-breakpoint
CREATE UNIQUE INDEX "ux_points_user_id" ON "points" USING btree ("user_id");--> statement-breakpoint
CREATE UNIQUE INDEX "unique_default_setting_per_user" ON "anki_settings" USING btree ("user_id") WHERE "anki_settings"."is_default" = true;--> statement-breakpoint
CREATE UNIQUE INDEX "unique_setting_user" ON "anki_settings" USING btree ("anki_setting_id","user_id");--> statement-breakpoint
CREATE UNIQUE INDEX "unique_user_topic" ON "user_topic_settings" USING btree ("user_id","topic_id");