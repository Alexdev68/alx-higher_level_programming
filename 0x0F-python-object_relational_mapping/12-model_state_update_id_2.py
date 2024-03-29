#!/usr/bin/python3
"""This script changes the name of a State object from the database
   hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
        argv[1], argv[2], "localhost", 3306, argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()

    h = session.query(State).get(2)

    h.name = "New Mexico"

    session.commit()

    session.close()
