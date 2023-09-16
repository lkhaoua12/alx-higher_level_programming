#!/usr/bin/python3
"""join cities on states by states id"""

import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Setting the conection argument.
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Setting up the connection to the MySQL server.
    url = f'mysql://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)

    # Creating a session to interact with the database.
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Querying and fetching City objects sorted by cities.id.
    city_state_info = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id
    ).order_by(City.id).all()

    # Displaying the results.
    for state_name, city_id, city_name in city_state_info:
        print(f"{state_name}: ({city_id}) {city_name}")

    # Closing the session.
    session.close()
