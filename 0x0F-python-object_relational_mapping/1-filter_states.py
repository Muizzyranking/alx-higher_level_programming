#!/usr/bin/python3
""" List all states that start with 'N' """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    sql_db = argv[3]

    db = MySQLdb.connect(user=sql_user, passwd=sql_pass, db=sql_db)
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
