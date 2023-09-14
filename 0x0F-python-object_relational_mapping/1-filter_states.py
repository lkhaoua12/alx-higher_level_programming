#!/usr/bin/python3
"""
    This script connects to a MySQL database.
    Usage:
        ./script_name.py <username> <password> <database_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cur = db.cursor()
    cur.execute("select * from states where name like 'N%' order by id ASC")
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
