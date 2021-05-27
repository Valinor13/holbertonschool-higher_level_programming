-- Lists all cities of California in database

SELECT id, name FROM cities WHERE state_id IN(
	SELECT id, name FROM states WHERE name = 'California') ORDER BY cities.id ASC;
