#!/usr/bin/python3
"""
    This script connects to a MySQL database and retrieves
    data from the 'cities' and 'states' tables.
    It then prints the retrieved data.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments for username, password, and dbname.
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

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
    cur.execute("SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id WHERE states.name = %s\
                ORDER BY cities.id", (state_name,))

    cities_list = cur.fetchall()
    cities = [city[0] for city in cities_list]
    print(', '.join(cities))

    # Closing the conection
    cur.close()
    db.close()
