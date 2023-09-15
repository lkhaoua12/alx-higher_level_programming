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
    cur.execute('select states.id from states where name = %s', (state_name,))
    state_row = cur.fetchone()

    if state_row:
        state_id = state_row[0]

        # Execute the SQL query to select cities in the specified state.
        cur.execute('SELECT name FROM cities WHERE state_id = %s', (state_id,))

        # Fetch all the rows from the result set.
        result = cur.fetchall()

        # Print the retrieved data.
        city_list = [row[0] for row in result]
        city_names = (', ').join(city_list)
        print(city_names)

    # Closing the conection
    cur.close()
    db.close()
