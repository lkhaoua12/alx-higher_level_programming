#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # getting the argument to pass to the engine
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # setting the connection to mysql
    url_s = f'mysql://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url_s)

    # starting a session to interacte with th db
    Base.metadata.create_all(engine)
    session = Session(engine)

    # fetching the required data.
    state = session.query(State).order_by(State.id).first()

    # print the state name
    print(f'{state.id}: {state.name}')

    # closing the session
    session.close()
