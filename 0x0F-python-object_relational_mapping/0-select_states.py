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
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
