#!/usr/bin/python3

"""
Script to list all states
from database hbtn_0e_0usa
Filtering those with a name starting with upper 'N'
"""

import MySQLdb
import sys

if "__main__" == __name__:
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
