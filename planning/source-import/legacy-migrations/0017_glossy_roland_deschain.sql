ALTER TABLE "flashcards" ADD COLUMN "is_star" boolean DEFAULT false NOT NULL;--> statement-breakpoint
ALTER TABLE "class_quizzes" ADD COLUMN "auto_publish_error" text;--> statement-breakpoint
ALTER TABLE "class_quizzes" ADD COLUMN "auto_publish_last_tried_at" timestamp with time zone;