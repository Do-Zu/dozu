-- Adds composite unique index to support ON CONFLICT upsert in feature usage tracking
CREATE UNIQUE INDEX IF NOT EXISTS user_feature_usage_user_id_feature_id_reset_period_start_idx
    ON "user_feature_usage" ("user_id", "feature_id", "reset_period_start");
