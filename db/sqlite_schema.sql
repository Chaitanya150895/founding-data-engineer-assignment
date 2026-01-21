-- sqlite_schema.sql - analytics schema
CREATE TABLE IF NOT EXISTS user_stats (
  user_id TEXT PRIMARY KEY,
  last_active TIMESTAMP,
  message_count INTEGER
);
