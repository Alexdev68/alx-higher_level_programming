#!/usr/bin/python3
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

    cur.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
        """,
        (argv[4],))

    rows = cur.fetchall()

    new_str = ''

    for row in rows:
        new_str += str(row)

    new_str = new_str.replace('(', '').replace(')', ' ').replace("'", '')
    new_str = new_str[:-2]
    print(new_str)

    cur.close()
    db.close()
