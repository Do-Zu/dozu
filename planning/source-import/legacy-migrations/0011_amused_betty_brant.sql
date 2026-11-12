ALTER TABLE "class_topic_comments"
ALTER COLUMN "topic_id" DROP NOT NULL;
--> statement-breakpoint
ALTER TABLE "class_topic_comments"
ALTER COLUMN "node_type"
SET DATA TYPE varchar(50);
--> statement-breakpoint
DROP TYPE "public"."node_type";