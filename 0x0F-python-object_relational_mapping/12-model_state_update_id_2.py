#!/usr/bin/python3
"""inssert state name passed as argument"""

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

    # setting the connection to the msql server
    url = f'mysql://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)

    # setting a session to interacte with the db
    Base.metadata.create_all(engine)
    session = Session(engine)

    # fetching the state to update it name
    state_update = session.query(State).filter(State.id == 2).first()
    if state_update:
        state_update.name = 'New Mexico'

        # commiting the update to the db
        session.commit()

    # closing the session
    session.close()
