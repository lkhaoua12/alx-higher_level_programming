#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Getting the MySQL connection parameters.
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Setting up the database connection.
    db_url = f'mysql://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(db_url)

    # Creating a session to interact with the database.
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Fetching the data.
    states = session.query(State).order_by(State.id).all()

    # Printing the states list.
    for state in states:
        print(f'{state.id}: {state.name}')

    # Ending the session.
    session.close()
