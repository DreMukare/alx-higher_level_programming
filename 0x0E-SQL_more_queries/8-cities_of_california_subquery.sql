-- lists all the Cities of Carlifornia in hbtn_0d_usa
SELECT cities_id, name AS id
FROM cities
WHERE cities.state_id = states.id
AND state.name = California;
