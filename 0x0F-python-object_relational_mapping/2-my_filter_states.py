#!/usr/bin/python3
"""This module displays all values in the states table of hbtn_0e_0_usa where
   name matches the argument."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()
    state = argv[4]

    cur.execute(
            "SELECT * FROM states WHERE name = '{}' ORDER BY states.id"
            .format(state)
            )

    rows = cur.fetchall()

    for row in rows:
        if state in str(row):
            print(f"{row}")

    cur.close()
    db.close()
