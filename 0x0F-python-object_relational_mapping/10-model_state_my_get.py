#!/usr/bin/python3
"""find state name passed as argument"""

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
    st_name = sys.argv[4]

    # Setting the connection to mysql server
    url = f'mysql://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)

    # Creating a session to access the db
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Fetching the data
    states = session.query(State).filter(State.name == st_name)

    # Printing the data
    if states.count() > 0:
        for state in states:
            print(f'{state.id}')
    else:
        print('Not found')

    # Closing the session
    session.close()
