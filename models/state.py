#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage
import models
import os


class State(BaseModel, Base):
    """State class."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') != 'db':
        cities = relationship('City', cascade='all, delete', backref='states')

        @property
        def cities(self):
            final = []
            city_list = models.storage.all(City)
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    final.append(city)
            return final
