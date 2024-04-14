#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa 
    usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

from sys import argv
import MySQLdb

user = argv[1]
passwd = argv[2]
db = argv[3]

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=user, passwd=passwd, db=db, charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
