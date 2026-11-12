CREATE TABLE "embeddings" (
	"embedding_id" serial PRIMARY KEY NOT NULL,
	"topic_id" integer NOT NULL,
	"embedding" vector(384) NOT NULL,
	"origin_content" jsonb NOT NULL,
	"content_type" varchar(50) NOT NULL,
	"metadata" jsonb DEFAULT '{}'::jsonb NOT NULL,
	"chunk_index" integer DEFAULT 0 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
ALTER TABLE "embeddings" ADD CONSTRAINT "embeddings_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE INDEX "embedding_vector_idx" ON "embeddings" USING hnsw ("embedding" vector_cosine_ops);--> statement-breakpoint
CREATE INDEX "embeddings_topic_id_idx" ON "embeddings" USING btree ("topic_id");