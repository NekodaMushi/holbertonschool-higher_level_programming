#!/usr/bin/python3
""" Lists all cities from the database by states """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name\
            FROM cities INNER JOIN states\
            ON states.id = cities.state_id\
            WHERE states.name = %(state)s\
            ORDER BY cities.id ASC", {'state': sys.argv[4]})
    city = [cities[0] for cities in c.fetchall()]
    print(", ".join(city))
    c.close()
    db.close()
