#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name))

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Create California state
    california = State(name="California")

    # Create San Francisco city
    san_francisco = City(name="San Francisco", state=california)

    # Add the state and city to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
