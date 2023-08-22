#!/usr/bin/python3
"""This script prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
        argv[1], argv[2], "localhost", 3306, argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()

    rows = session.query(State).order_by(State.id).all()

    for row in rows:
        print("{}: {}".format(row.id, row.name))
        for city in row.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
