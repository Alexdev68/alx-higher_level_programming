#!/usr/bin/python3
"""This script adds deletes all State objects with a name containing the
   letter a from the database hbtn_0e_6_usa
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

    session.query(State).filter(State.name.like('%a%')).delete(
            synchronize_session=False)
    session.commit()

    session.close()
