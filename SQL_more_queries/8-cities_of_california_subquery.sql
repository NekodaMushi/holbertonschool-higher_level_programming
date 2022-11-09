-- Lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id FROM cities
WHERE states IN (
    SELECT id
    FROM states
    WHERE name = California
);
