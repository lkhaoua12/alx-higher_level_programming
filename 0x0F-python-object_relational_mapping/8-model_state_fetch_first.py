#!/usr/bin/python3
"""fetch the first object of the state clss"""

import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # getting the connection arg
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # setting the connection to the msql_server
    url = f'mysql://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)

    # creating a session to interacete with the db.
    Base.metadata.create_all(engine)
    session = Session(engine)

    # fetching the data.
    state = session.query(State).order_by(State.id).first()

    # print the data
    print(f'{state.id}: {state.name}')

    # closing the session
    session.close()
