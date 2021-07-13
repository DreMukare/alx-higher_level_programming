-- lists all the Cities of Carlifornia in hbtn_0d_usa
SELECT cities_id AS id, name
FROM cities
WHERE state_id =
	(SELECT id 
	 FROM states
	 WHERE name = California);
