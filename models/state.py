#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """State class."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') != 'db':
        cities = relationship('City', cascade='all, delete', backref='states')

    else:
        @property
        def cities(self):
            """Is function "cities" is not defined and therefore cannot be\
            summarized."""
            from models import storage

            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
