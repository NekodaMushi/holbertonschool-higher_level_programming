-- Script that list all cities contained in database hbtn_0d_2
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY id ASC;
