CREATE TYPE "public"."content_type" AS ENUM('topic', 'quiz', 'flashcard');--> statement-breakpoint
CREATE TYPE "public"."progress_status" AS ENUM('not_started', 'in_progress', 'completed', 'failed');--> statement-breakpoint
ALTER TYPE "public"."item_status_type" ADD VALUE 'relearning';--> statement-breakpoint
CREATE TABLE "progress" (
	"progress_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"topic_id" integer NOT NULL,
	"content_type" "content_type" NOT NULL,
	"completion_percentage" integer DEFAULT 0 NOT NULL,
	"status" "progress_status" NOT NULL,
	"score" double precision,
	"metadata" jsonb,
	"last_interaction_at" timestamp with time zone DEFAULT now(),
	"created_at" timestamp with time zone DEFAULT now(),
	"updated_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "daily_study_records" (
	"daily_study_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"date" date NOT NULL,
	"total_minutes" integer DEFAULT 0 NOT NULL,
	"sessions_count" integer DEFAULT 1 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now(),
	"updated_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
ALTER TABLE "item_spaced_repetition_tracking" ALTER COLUMN "last_reviewed" SET DATA TYPE timestamp with time zone;--> statement-breakpoint
ALTER TABLE "item_spaced_repetition_tracking" ALTER COLUMN "next_review" SET DATA TYPE timestamp with time zone;--> statement-breakpoint
ALTER TABLE "item_spaced_repetition_tracking" ADD COLUMN "step" integer;--> statement-breakpoint
ALTER TABLE "progress" ADD CONSTRAINT "progress_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "progress" ADD CONSTRAINT "progress_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "daily_study_records" ADD CONSTRAINT "daily_study_records_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;