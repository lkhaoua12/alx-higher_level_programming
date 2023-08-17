-- 16-no_link.sql
-- list where record isnt null
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
