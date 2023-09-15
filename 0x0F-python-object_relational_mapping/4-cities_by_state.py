#!/usr/bin/python3
import MySQLdb
import sys

"""
    This script connects to a MySQL database and retrieves
    data from the 'cities' and 'states' tables.
    It then prints the retrieved data.
"""

if __name__ == "__main__":
    # Get command-line arguments for username, password, and dbname.
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to the MySQL database.
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    # Create a cursor object for executing SQL queries.
    cur = db.cursor()

    # Execute the SQL query to select data from cities and states tables.
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 ORDER BY cities.id ASC')

    # Fetch all the rows from the result set.
    result = cur.fetchall()

    # Print the retrieved data.
    for row in result:
        print(row)
