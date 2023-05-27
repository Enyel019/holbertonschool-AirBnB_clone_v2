#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage
import os


class State(BaseModel, Base):
    """State class."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') != 'db':
        cities = relationship('City', cascade='all, delete', backref='state')

    else:
        @property
        def cities(self):
            """
            The function "cities" is not defined and therefore cannot be/
            summarized.
            """
            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
