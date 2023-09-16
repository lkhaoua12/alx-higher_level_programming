#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # getting the connection parameters.
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # establishing a conection to the database.
    url_s = f'mysql://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url_s)

    # create a session to interacte with the database
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Fetching the Data.
    states = session.query(State)\
                    .filter(State.name.like('%a%'))\
                    .order_by(State.id).all()

    # printing the result.
    for state in states:
        print(f'{state.id}: {state.name}')

    # closing the session
    session.close()
