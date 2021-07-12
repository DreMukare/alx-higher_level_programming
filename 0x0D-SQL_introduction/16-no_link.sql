-- lists all the records with a name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
