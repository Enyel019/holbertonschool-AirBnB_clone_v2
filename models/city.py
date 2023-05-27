#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class City(BaseModel, Base):
    """This is a Python class that inherits from two other classes/
       BaseModel and Base, and represents a
       city."""

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False)
