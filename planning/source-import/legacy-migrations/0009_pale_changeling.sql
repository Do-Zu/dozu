CREATE TYPE "public"."assignment_status_type" AS ENUM('draft', 'scheduled', 'published', 'closed');--> statement-breakpoint
CREATE TYPE "public"."submission_status_type" AS ENUM('draft', 'submitted', 'returned');--> statement-breakpoint
CREATE TABLE "attachment" (
	"attachment_id" serial PRIMARY KEY NOT NULL,
	"title" varchar(255) NOT NULL,
	"description" varchar(255),
	"content_type" varchar(50),
	"metadata" jsonb,
	"created_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "packages" (
	"id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"title" varchar(255) NOT NULL,
	"parent_id" integer,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "question_result" (
	"quiz_id" integer NOT NULL,
	"question_id" integer NOT NULL,
	"user_id" integer NOT NULL,
	"correct" boolean NOT NULL,
	"user_answer_index" integer,
	"answered_at" timestamp with time zone DEFAULT now(),
	CONSTRAINT "question_result_quiz_id_question_id_user_id_pk" PRIMARY KEY("quiz_id","question_id","user_id")
);
--> statement-breakpoint
CREATE TABLE "assignments" (
	"assignment_id" serial PRIMARY KEY NOT NULL,
	"teacher_id" integer NOT NULL,
	"class_id" integer NOT NULL,
	"topic_id" integer,
	"title" varchar(255) NOT NULL,
	"content" text DEFAULT '' NOT NULL,
	"deadline" timestamp with time zone,
	"total_grades" integer DEFAULT 100 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone,
	"published_at" timestamp with time zone,
	"status" "assignment_status_type" DEFAULT 'draft' NOT NULL,
	"accepting_submissions" boolean NOT NULL
);
--> statement-breakpoint
CREATE TABLE "assignment_submissions" (
	"submission_id" serial PRIMARY KEY NOT NULL,
	"assignment_id" integer NOT NULL,
	"student_id" integer NOT NULL,
	"grade" integer,
	"submitted_at" timestamp with time zone,
	"updated_at" timestamp with time zone,
	"returned_at" timestamp with time zone,
	"status" "submission_status_type" DEFAULT 'draft' NOT NULL
);
--> statement-breakpoint
CREATE TABLE "assignment_comments" (
	"comment_id" serial PRIMARY KEY NOT NULL,
	"assignment_id" integer,
	"submission_id" integer NOT NULL,
	"sender_id" integer NOT NULL,
	"content" text DEFAULT '' NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone
);
--> statement-breakpoint
ALTER TABLE "topics" ADD COLUMN "package_id" integer;--> statement-breakpoint
ALTER TABLE "packages" ADD CONSTRAINT "packages_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "packages" ADD CONSTRAINT "packages_parent_id_fkey" FOREIGN KEY ("parent_id") REFERENCES "public"."packages"("id") ON DELETE set null ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "question_result" ADD CONSTRAINT "question_result_quiz_id_quizzes_quiz_id_fk" FOREIGN KEY ("quiz_id") REFERENCES "public"."quizzes"("quiz_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "question_result" ADD CONSTRAINT "question_result_question_id_questions_question_id_fk" FOREIGN KEY ("question_id") REFERENCES "public"."questions"("question_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "question_result" ADD CONSTRAINT "question_result_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignments" ADD CONSTRAINT "assignments_teacher_id_users_user_id_fk" FOREIGN KEY ("teacher_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignments" ADD CONSTRAINT "assignments_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignments" ADD CONSTRAINT "assignments_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_submissions" ADD CONSTRAINT "assignment_submissions_assignment_id_assignments_assignment_id_fk" FOREIGN KEY ("assignment_id") REFERENCES "public"."assignments"("assignment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_submissions" ADD CONSTRAINT "assignment_submissions_student_id_users_user_id_fk" FOREIGN KEY ("student_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_comments" ADD CONSTRAINT "assignment_comments_assignment_id_assignments_assignment_id_fk" FOREIGN KEY ("assignment_id") REFERENCES "public"."assignments"("assignment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_comments" ADD CONSTRAINT "assignment_comments_submission_id_assignment_submissions_submission_id_fk" FOREIGN KEY ("submission_id") REFERENCES "public"."assignment_submissions"("submission_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_comments" ADD CONSTRAINT "assignment_comments_sender_id_users_user_id_fk" FOREIGN KEY ("sender_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE UNIQUE INDEX "unique_student_assignment" ON "assignment_submissions" USING btree ("assignment_id","student_id");--> statement-breakpoint
ALTER TABLE "topics" ADD CONSTRAINT "topics_package_id_packages_id_fk" FOREIGN KEY ("package_id") REFERENCES "public"."packages"("id") ON DELETE set null ON UPDATE no action;