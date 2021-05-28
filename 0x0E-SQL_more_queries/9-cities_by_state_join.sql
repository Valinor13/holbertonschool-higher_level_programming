-- Lists all cities contained in database.
-- hbtn_0d_usa

SELECT *
FROM states
INNER JOIN cities
ON cities.id = states.id 
ORDER BY
cities.id ASC;
