CREATE TYPE "public"."invite_status" AS ENUM('pending', 'accepted', 'rejected', 'expired');--> statement-breakpoint
CREATE TYPE "public"."class_quiz_status" AS ENUM('draft', 'scheduled', 'published', 'closed');--> statement-breakpoint
CREATE TYPE "public"."class_quiz_attempt_status" AS ENUM('in_progress', 'submitted', 'cancelled');--> statement-breakpoint
CREATE TABLE "class_invites" (
	"invite_id" serial PRIMARY KEY NOT NULL,
	"class_id" integer NOT NULL,
	"invited_by" integer NOT NULL,
	"invited_user_id" integer,
	"invited_email" varchar(100),
	"token" varchar(50) NOT NULL,
	"status" "invite_status" DEFAULT 'pending' NOT NULL,
	"expires_at" timestamp with time zone NOT NULL,
	"use_limit" integer,
	"used_count" integer DEFAULT 0 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone,
	CONSTRAINT "class_invites_token_unique" UNIQUE("token")
);
--> statement-breakpoint
CREATE TABLE "class_quizzes" (
	"class_quiz_id" serial PRIMARY KEY NOT NULL,
	"teacher_id" integer NOT NULL,
	"class_id" integer NOT NULL,
	"topic_id" integer,
	"title" varchar(255) NOT NULL,
	"content" text DEFAULT '' NOT NULL,
	"start_at" timestamp with time zone,
	"end_at" timestamp with time zone,
	"duration_seconds" integer,
	"max_attempts" integer DEFAULT 1 NOT NULL,
	"shuffle_questions" boolean DEFAULT true NOT NULL,
	"shuffle_choices" boolean DEFAULT true NOT NULL,
	"show_score_to_student" boolean DEFAULT true NOT NULL,
	"accepting_submissions" boolean DEFAULT true NOT NULL,
	"status" "class_quiz_status" DEFAULT 'draft' NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone,
	"published_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "class_quiz_versions" (
	"class_quiz_version_id" serial PRIMARY KEY NOT NULL,
	"class_quiz_id" integer NOT NULL,
	"questions_snapshot" text NOT NULL,
	"choices_shuffle_seed" varchar(64),
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "class_quiz_attempts" (
	"attempt_id" serial PRIMARY KEY NOT NULL,
	"class_quiz_id" integer NOT NULL,
	"class_quiz_version_id" integer,
	"user_id" integer NOT NULL,
	"attempt_started_at" timestamp with time zone NOT NULL,
	"attempt_end_at" timestamp with time zone NOT NULL,
	"submitted_at" timestamp with time zone,
	"status" "class_quiz_attempt_status" DEFAULT 'in_progress' NOT NULL,
	"score" integer,
	"correct_count" integer,
	"questions_count" integer,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "class_quiz_attempt_answers" (
	"attempt_id" integer NOT NULL,
	"snapshot_question_idx" integer NOT NULL,
	"user_answer_index" integer,
	"correct" boolean DEFAULT false NOT NULL,
	"answered_at" timestamp with time zone DEFAULT now(),
	CONSTRAINT "class_quiz_attempt_answers_attempt_id_snapshot_question_idx_pk" PRIMARY KEY("attempt_id","snapshot_question_idx")
);
--> statement-breakpoint
CREATE TABLE "class_quiz_drafts" (
	"class_quiz_id" integer PRIMARY KEY NOT NULL,
	"teacher_id" integer NOT NULL,
	"draft_json" jsonb NOT NULL,
	"version" integer DEFAULT 1 NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "assignment_attachments" (
	"attachment_id" integer NOT NULL,
	"assignment_id" integer NOT NULL,
	CONSTRAINT "assignment_attachments_attachment_id_assignment_id_pk" PRIMARY KEY("attachment_id","assignment_id")
);
--> statement-breakpoint
CREATE TABLE "assignment_submission_attachments" (
	"attachment_id" integer NOT NULL,
	"assignment_submission_id" integer NOT NULL,
	CONSTRAINT "assignment_submission_attachments_attachment_id_assignment_submission_id_pk" PRIMARY KEY("attachment_id","assignment_submission_id")
);
--> statement-breakpoint
CREATE TABLE "learning_materials" (
	"learning_material_id" serial PRIMARY KEY NOT NULL,
	"title" varchar(255) NOT NULL,
	"description" varchar(255),
	"topic_id" integer,
	"class_id" integer NOT NULL,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "attachment_in_learning_material" (
	"attachment_id" integer NOT NULL,
	"learning_material_id" integer NOT NULL,
	CONSTRAINT "attachment_in_learning_material_attachment_id_learning_material_id_pk" PRIMARY KEY("attachment_id","learning_material_id")
);
--> statement-breakpoint
DROP TABLE "assignment_comments" CASCADE;--> statement-breakpoint
ALTER TABLE "class_invites" ADD CONSTRAINT "class_invites_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_invites" ADD CONSTRAINT "class_invites_invited_by_users_user_id_fk" FOREIGN KEY ("invited_by") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_invites" ADD CONSTRAINT "class_invites_invited_user_id_users_user_id_fk" FOREIGN KEY ("invited_user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_quizzes" ADD CONSTRAINT "class_quizzes_teacher_id_users_user_id_fk" FOREIGN KEY ("teacher_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_quizzes" ADD CONSTRAINT "class_quizzes_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_quizzes" ADD CONSTRAINT "class_quizzes_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_quiz_versions" ADD CONSTRAINT "class_quiz_versions_class_quiz_id_class_quizzes_class_quiz_id_fk" FOREIGN KEY ("class_quiz_id") REFERENCES "public"."class_quizzes"("class_quiz_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_quiz_attempts" ADD CONSTRAINT "class_quiz_attempts_class_quiz_id_class_quizzes_class_quiz_id_fk" FOREIGN KEY ("class_quiz_id") REFERENCES "public"."class_quizzes"("class_quiz_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_quiz_attempts" ADD CONSTRAINT "class_quiz_attempts_class_quiz_version_id_class_quiz_versions_class_quiz_version_id_fk" FOREIGN KEY ("class_quiz_version_id") REFERENCES "public"."class_quiz_versions"("class_quiz_version_id") ON DELETE set null ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_quiz_attempts" ADD CONSTRAINT "class_quiz_attempts_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_quiz_attempt_answers" ADD CONSTRAINT "class_quiz_attempt_answers_attempt_id_class_quiz_attempts_attempt_id_fk" FOREIGN KEY ("attempt_id") REFERENCES "public"."class_quiz_attempts"("attempt_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_quiz_drafts" ADD CONSTRAINT "class_quiz_drafts_class_quiz_id_class_quizzes_class_quiz_id_fk" FOREIGN KEY ("class_quiz_id") REFERENCES "public"."class_quizzes"("class_quiz_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_quiz_drafts" ADD CONSTRAINT "class_quiz_drafts_teacher_id_users_user_id_fk" FOREIGN KEY ("teacher_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_attachments" ADD CONSTRAINT "assignment_attachments_attachment_id_attachment_attachment_id_fk" FOREIGN KEY ("attachment_id") REFERENCES "public"."attachment"("attachment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_attachments" ADD CONSTRAINT "assignment_attachments_assignment_id_assignments_assignment_id_fk" FOREIGN KEY ("assignment_id") REFERENCES "public"."assignments"("assignment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_submission_attachments" ADD CONSTRAINT "assignment_submission_attachments_attachment_id_attachment_attachment_id_fk" FOREIGN KEY ("attachment_id") REFERENCES "public"."attachment"("attachment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_submission_attachments" ADD CONSTRAINT "assignment_submission_attachments_assignment_submission_id_assignment_submissions_submission_id_fk" FOREIGN KEY ("assignment_submission_id") REFERENCES "public"."assignment_submissions"("submission_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "learning_materials" ADD CONSTRAINT "learning_materials_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "learning_materials" ADD CONSTRAINT "learning_materials_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "attachment_in_learning_material" ADD CONSTRAINT "attachment_in_learning_material_attachment_id_attachment_attachment_id_fk" FOREIGN KEY ("attachment_id") REFERENCES "public"."attachment"("attachment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "attachment_in_learning_material" ADD CONSTRAINT "attachment_in_learning_material_learning_material_id_learning_materials_learning_material_id_fk" FOREIGN KEY ("learning_material_id") REFERENCES "public"."learning_materials"("learning_material_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE INDEX "idx_cqaa_attempt" ON "class_quiz_attempt_answers" USING btree ("attempt_id");--> statement-breakpoint
CREATE INDEX "idx_cqd_teacher" ON "class_quiz_drafts" USING btree ("teacher_id");