#!/usr/bin/python3
"""delete states that include a in the name"""

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
    state_delete = session.query(State).filter(State.name.like('%a%')).all()
    if state_delete:
        for state in state_delete:
            session.delete(state)

        # commiting the update to the db
        session.commit()

    # closing the session
    session.close()
