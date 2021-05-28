-- Lists all cities contained in database.
-- hbtn_0d_usa

SELECT cities.id, cities.name, states.name 
FROM cities
INNER JOIN states
ON states.id = cities.id 
ORDER BY
cities.id ASC;
