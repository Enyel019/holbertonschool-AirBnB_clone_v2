#!/usr/bin/python3
"""Place Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
import models
import os


class Place(BaseModel, Base):
    """A place to stay."""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
        
    # For DBStorage
    if models.storage_type == 'db':
        reviews = relationship('Review', cascade='all, delete-orphan', backref='place')

    # For FileStorage
    else:
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances
            with place_id equals to the current Place.id"""
            review_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list