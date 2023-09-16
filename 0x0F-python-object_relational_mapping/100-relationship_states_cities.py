#!/usr/bin/python3
"""Create new tables and link them."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Getting connection parameters.
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Setting up the connection to the MySQL server.
    url = f'mysql://{username}:{password}@localhost:3306/{db_name}'
    engine = create_engine(url)

    # Setting up the session to interacte with the db
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Creating the new State object for California.
    california = State(name="California")

    # Creating a new City object for San Francisco.
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    # Adding California to the session and committing the changes.
    session.add(california)
    session.commit()

    # Closing the session.
    session.close()
