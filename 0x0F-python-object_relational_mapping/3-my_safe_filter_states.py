#!/usr/bin/python3
""" safely List all states that start with 'N' """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    sql_db = argv[3]
    search_state = argv[4]

    db = MySQLdb.connect(user=sql_user, passwd=sql_pass, db=sql_db)
    cursor = db.cursor()
    statement = """
        SELECT * FROM states WHERE name = %s ORDER BY id ASC
        """
    cursor.execute(statement, (search_state, ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
