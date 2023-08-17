-- 15-groups.sql
-- display record by grouping
SELECT score, count(*) AS number FROM second_table 
GROUP BY score ORDER BY DESC;
