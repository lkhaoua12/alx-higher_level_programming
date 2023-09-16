#!/usr/bin/python3
"""find state name with the letter a in it"""

import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Getting connection parameters.
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Setting the connection to mysql server
    url = f'mysql://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)

    # Creating a session to access the db
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Fetching the data
    states = session.query(State).filter(State.name.like('%a%'))

    # Printing the data
    for state in states:
        print(f'{state.id}: {state.name}')

    # Closing the session
    session.close()
