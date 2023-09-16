#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database hbtn_0e_6_usa"""

import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # get the conection arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # setting up the conection to mysql
    url = f'mysql://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)

    # creating a session to interacte with the database
    Base.metadata.create_all(engine)
    session = Session(engine)

    # adding the new state to the db
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # printing the new_state id
    print(new_state.id)

    # Close the session
    session.close()
