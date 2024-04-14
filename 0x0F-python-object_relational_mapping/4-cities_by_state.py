#!/usr/bin/python3
""" List all cities by state """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    sql_db = argv[3]

    db = MySQLdb.connect(user=sql_user, passwd=sql_pass, db=sql_db)
    cursor = db.cursor()
    cursor.execute(
        """SELECT
            cities.id, cities.name, states.name
            FROM cities INNER JOIN states on cities.state_id = states.id
            ORDER by cities.id asc, states.name asc; """
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
