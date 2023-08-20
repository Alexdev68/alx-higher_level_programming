#!/usr/bin/python3
"""This module contains the class definition of a State and an instance
   Base = declarative_base()."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user = "root"
host = "localhost"
port = 3306
password = "root"
db_name = "hbtn_0e_6_usa"


class State(Base):
    """This is the class that inherits from base."""

    __tablename__ = "states"
    """This defines the name of the table"""

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


engine = create_engine(url="mysql+mysqldb://{}:{}@{}:{}/{}".format(
    user, password, host, port, db_name))

Base.metadata.create_all(engine)
