#!/usr/bin/python3
"""Create California with San Francisco"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a new session
    session = Session(engine)

    # Create California and San Francisco
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # Add to the session and commit
    session.add(new_state)
    session.commit()

    # Clean up
    session.close()
