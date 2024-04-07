-- lists all cities in california in database
SELECT
  `id`,
  `name`
FROM
  cities
WHERE
  state_id = (
    SELECT
      `id`
    FROM
      states
    WHERE
      name = 'California'
  )
ORDER By
  cities.id ASC;
