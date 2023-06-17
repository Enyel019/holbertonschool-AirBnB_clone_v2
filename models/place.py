#!/usr/bin/python3
"""This is the place class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from os import getenv
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place."""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Unfortunately, there is no code provided for the function, so I\
            cannot provide a summary."""
            list_return = []
            for key_, value_ in models.storage.all(Review).items():
                if value_.place_id == self.id:
                    list_return.append(value_)
            return (list_return)

        @property
        def amenities(self):
            """The function "amenities" is defined but its implementation\
            is missing."""
            list_return = []
            for key__, value__ in models.storage.all(Amenity).items():
                if value__.place_id == self.id:
                    list_return.append(values)
            return (list_return)

        @amenities.setter
        def amenities(self, value):
            if 'Amenity' in value:
                self.amenity_ids.append(value)
