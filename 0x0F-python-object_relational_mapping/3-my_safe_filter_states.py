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
    state_name = str(sys.argv[4])

    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=dbname
        )

        cur = db.cursor()
        ex_query = "SELECT * FROM states WHERE name = %s"
        cur.execute(ex_query, (state_name,))

        result = cur.fetchall()

        for row in result:
            print(row)

    except MySQLdb.Error as e:
        print(f"Database Error: {e}")
    finally:
        if cur:
            cur.close()
        if db:
            db.close()
