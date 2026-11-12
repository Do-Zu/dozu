CREATE TYPE "public"."feed_type" AS ENUM('announcement', 'new_content');--> statement-breakpoint
CREATE TABLE "change_password_requests" (
	"change_password_request_id" serial PRIMARY KEY NOT NULL,
	"user_id" integer NOT NULL,
	"verification_code" text NOT NULL,
	"expiration" timestamp with time zone NOT NULL,
	CONSTRAINT "change_password_requests_verification_code_unique" UNIQUE("verification_code")
);
--> statement-breakpoint
CREATE TABLE "class_feeds" (
	"class_feed_id" serial PRIMARY KEY NOT NULL,
	"class_id" integer NOT NULL,
	"sender_id" integer NOT NULL,
	"type" "feed_type" DEFAULT 'announcement' NOT NULL,
	"title" varchar(255) NOT NULL,
	"content" text DEFAULT '' NOT NULL,
	"link" text,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone
);
--> statement-breakpoint
ALTER TABLE "change_password_requests" ADD CONSTRAINT "change_password_requests_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_feeds" ADD CONSTRAINT "class_feeds_class_id_classes_class_id_fk" FOREIGN KEY ("class_id") REFERENCES "public"."classes"("class_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "class_feeds" ADD CONSTRAINT "class_feeds_sender_id_users_user_id_fk" FOREIGN KEY ("sender_id") REFERENCES "public"."users"("user_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE INDEX "change_password_request_user_id_idx" ON "change_password_requests" USING btree ("user_id");