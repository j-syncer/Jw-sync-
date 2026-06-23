-- Adds optional email to posts so authors can opt in to reply notifications.
-- Run this in the Supabase SQL editor before deploying the notification worker.
ALTER TABLE posts ADD COLUMN IF NOT EXISTS author_email TEXT;
