CREATE TABLE "feynman_sessions" (
	"id" serial PRIMARY KEY NOT NULL,
	"topic_id" integer NOT NULL,
	"method" varchar(50) NOT NULL,
	"explanation_text" text NOT NULL,
	"explanation_html" text NOT NULL,
	"highlighted_words" text[] DEFAULT ARRAY[]::text[] NOT NULL,
	"questions" jsonb NOT NULL,
	"review" jsonb DEFAULT 'null'::jsonb,
	"step" integer DEFAULT 1 NOT NULL,
	"version" integer DEFAULT 1,
	"saved_at" timestamp with time zone NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
ALTER TABLE "feynman_sessions" ADD CONSTRAINT "feynman_sessions_topic_id_topics_topic_id_fk" FOREIGN KEY ("topic_id") REFERENCES "public"."topics"("topic_id") ON DELETE cascade ON UPDATE no action;