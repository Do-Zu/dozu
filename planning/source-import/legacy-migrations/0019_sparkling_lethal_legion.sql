CREATE TABLE "class_streaks" (
	"class_streak_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"class_id" integer NOT NULL,
	"current_streak" integer DEFAULT 0 NOT NULL,
	"longest_streak" integer DEFAULT 0 NOT NULL,
	"last_study_date" timestamp with time zone,
	"streak_freeze_used" boolean DEFAULT false,
	"streak_freeze_count" integer DEFAULT 0 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now(),
	"updated_at" timestamp with time zone DEFAULT now()
);
--> statement-breakpoint
CREATE TABLE "streak_events" (
	"id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"class_id" integer NOT NULL,
	"event_date" timestamp with time zone NOT NULL,
	"event_type" varchar(50) NOT NULL,
	"points_awarded" integer DEFAULT 0 NOT NULL,
	"streak_count" integer NOT NULL,
	"is_processed" boolean DEFAULT false NOT NULL,
	"created_at" timestamp with time zone DEFAULT now(),
	CONSTRAINT "streak_events_user_id_class_id_event_date_unique" UNIQUE("user_id","class_id","event_date")
);
--> statement-breakpoint
CREATE TABLE "assignment_comments" (
	"assignment_comment_id" serial PRIMARY KEY NOT NULL,
	"comment_id" integer NOT NULL,
	"assignment_id" integer NOT NULL,
	"submission_id" integer
);
--> statement-breakpoint
CREATE TABLE "learning_material_comments" (
	"learning_material_comment_id" serial PRIMARY KEY NOT NULL,
	"comment_id" integer NOT NULL,
	"learning_material_id" integer NOT NULL
);
--> statement-breakpoint
CREATE TABLE "comments" (
	"comment_id" serial PRIMARY KEY NOT NULL,
	"sender_id" integer NOT NULL,
	"content" text DEFAULT '' NOT NULL,
	"parent_comment_id" integer,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone
);
--> statement-breakpoint
ALTER TABLE "user_subscriptions" DROP CONSTRAINT "user_subscriptions_user_id_fk";
--> statement-breakpoint
DROP INDEX "ux_points_user_id";--> statement-breakpoint
ALTER TABLE "learning_materials" ALTER COLUMN "content" SET DATA TYPE text;--> statement-breakpoint
ALTER TABLE "learning_materials" ALTER COLUMN "content" SET DEFAULT '';--> statement-breakpoint
ALTER TABLE "learning_materials" ALTER COLUMN "content" SET NOT NULL;--> statement-breakpoint
ALTER TABLE "point_transactions" ADD COLUMN "class_id" integer NOT NULL;--> statement-breakpoint
ALTER TABLE "points" ADD COLUMN "class_id" integer NOT NULL;--> statement-breakpoint
ALTER TABLE "user_achievements" ADD COLUMN "class_id" integer NOT NULL;--> statement-breakpoint
ALTER TABLE "assignments" ADD COLUMN "urls" varchar(2048)[];--> statement-breakpoint
ALTER TABLE "assignment_submissions" ADD COLUMN "urls" varchar(2048)[];--> statement-breakpoint
ALTER TABLE "learning_materials" ADD COLUMN "urls" varchar(2048)[];--> statement-breakpoint
ALTER TABLE "class_streaks" ADD CONSTRAINT "class_streaks_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_streaks" ADD CONSTRAINT "class_streaks_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "streak_events" ADD CONSTRAINT "streak_events_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "streak_events" ADD CONSTRAINT "streak_events_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_comments" ADD CONSTRAINT "assignment_comments_comment_id_comments_comment_id_fk" FOREIGN KEY ("comment_id") REFERENCES "public"."comments"("comment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_comments" ADD CONSTRAINT "assignment_comments_assignment_id_assignments_assignment_id_fk" FOREIGN KEY ("assignment_id") REFERENCES "public"."assignments"("assignment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "assignment_comments" ADD CONSTRAINT "assignment_comments_submission_id_assignment_submissions_submission_id_fk" FOREIGN KEY ("submission_id") REFERENCES "public"."assignment_submissions"("submission_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "learning_material_comments" ADD CONSTRAINT "learning_material_comments_comment_id_comments_comment_id_fk" FOREIGN KEY ("comment_id") REFERENCES "public"."comments"("comment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "learning_material_comments" ADD CONSTRAINT "learning_material_comments_learning_material_id_learning_materials_learning_material_id_fk" FOREIGN KEY ("learning_material_id") REFERENCES "public"."learning_materials"("learning_material_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "comments" ADD CONSTRAINT "comments_sender_id_users_user_id_fk" FOREIGN KEY ("sender_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "comments" ADD CONSTRAINT "comments_parent_comment_id_comments_comment_id_fk" FOREIGN KEY ("parent_comment_id") REFERENCES "public"."comments"("comment_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE UNIQUE INDEX "ux_class_streak_user_class" ON "class_streaks" USING btree ("user_id","class_id");--> statement-breakpoint
ALTER TABLE "user_subscriptions" ADD CONSTRAINT "user_subscriptions_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "point_transactions" ADD CONSTRAINT "point_transactions_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "points" ADD CONSTRAINT "points_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "user_achievements" ADD CONSTRAINT "user_achievements_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE UNIQUE INDEX "ux_points_user_class" ON "points" USING btree ("user_id","class_id");--> statement-breakpoint
CREATE UNIQUE INDEX "ux_user_achievement_class" ON "user_achievements" USING btree ("user_id","achievement_id","class_id");