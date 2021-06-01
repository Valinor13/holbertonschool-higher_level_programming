#!/usr/bin/python3
"""A module that contains City inherited from Base"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """A class that inherits from base for sqlalchemy"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
