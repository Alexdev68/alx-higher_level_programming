#!/usr/bin/python3
"""This script adds the State object “Louisiana” to the database hbtn_0e_6_usa.
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

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    rows = session.query(State).order_by(State.id).all()

    for row in rows:
        if row.name == 'Louisiana':
            print(row.id)

    session.close()
