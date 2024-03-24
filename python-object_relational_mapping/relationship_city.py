#!/usr/bin/python3
""" contains the class definition of a City """


from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ model City

     Attributes:
        id (sqlalchemy.Column): The city's id.
        name (sqlalchemy.Column): The city's name.
        state_id (sqlalchemy.Column): The city's state id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
