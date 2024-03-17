-- list records of a table if name is not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
