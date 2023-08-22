#!/usr/bin/python3
"""This script creates the State "California" with the City
   "San Francisco" from the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
        argv[1], argv[2], "localhost", 3306, argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    stat = State(name="California")
    cit = City(name="San Francisco", state=stat)

    session.add(stat)
    session.add(cit)
    session.commit()

    session.close()
