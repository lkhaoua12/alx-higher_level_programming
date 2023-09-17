#!/usr/bin/python3
"""Create California with San Francisco"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Getting the conection args.
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Setting the connection to the server.
    url = f'mysql://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)
    Base.metadata.create_all(engine)

    # Starting a session to interacte with the db.
    session = Session(engine)

    # Quering the data
    states = session.query(State).order_by(State.id).all()

    # Displaying the data.
    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'\t{city.id}: {city.name}')

    # closing the session.
    session.close()
