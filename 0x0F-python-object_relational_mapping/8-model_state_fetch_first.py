#!/usr/bin/python3
"""This module lists all states objects from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
        user, password, host, port, db_name))
    Session = sessionmaker(bind=engine)

    session = Session()

    rows = session.query(State).order_by(State.id).first()

    if rows is not None:
        print("{}: {}".format(rows.id, rows.name))
    else:
        print('')

    session.close()
