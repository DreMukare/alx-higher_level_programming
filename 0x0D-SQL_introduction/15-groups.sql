-- lists the number of records with the same score
SELECT score, COUNT(score) AS count
FROM second_table
GROUP BY score
ORDER BY count DESC;
