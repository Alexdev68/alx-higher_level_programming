#!/usr/bin/python3
"""This script lists all City objects from the database hbtn_0e_101_usa.
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}")
    Session = sessionmaker(bind=engine)

    session = Session()

    rows = session.query(State).order_by(State.id).all()

    for row in rows:
        for city in row.cities:
            print(f"{city.id}: {city.name} -> {row.name}")
