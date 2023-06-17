#!/usr/bin/python3
"""This is the amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This is the class for Amenity."""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("PlaceAmenity", back_populates="amenity")
