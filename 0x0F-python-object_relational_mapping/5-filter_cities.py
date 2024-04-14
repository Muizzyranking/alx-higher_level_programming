#!/usr/bin/python3
""" List all cities by state with filter"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    sql_db = argv[3]
    search_state = argv[4]

    db = MySQLdb.connect(user=sql_user, passwd=sql_pass, db=sql_db)
    cursor = db.cursor()
    statement = """SELECT
            cities.name
            FROM cities INNER JOIN states on cities.state_id = states.id
            WHERE states.name = %s
            """
    cursor.execute(statement, (search_state,))

    rows = cursor.fetchall()
    # Convert the first element of each tuple to a string
    formatted_output = ", ".join(str(row[0]) for row in rows)
    print(formatted_output)
    cursor.close()
    db.close()
