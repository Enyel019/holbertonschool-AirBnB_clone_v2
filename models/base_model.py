#!/usr/bin/python3
"""This is the base model class for AirBnB."""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage


Base = declarative_base()


class BaseModel:
    """The above class is a base model that can be inherited
    by other classes."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        This is the constructor method for a Python class that takes any/
        number of arguments and keyword
        arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.utcnow()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.utcnow()

    def save(self):
        """
        The function "save" is defined, but its implementation is not shown.
        """
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        """
        The function "delete" is defined, but its implementation is missing.
        """
        storage.delete(self)

    def to_dict(self):
        """
        The function "to_dict" is likely a method of a class in Python that/
        returns a dictionary
        representation of an object.
        """
        dict_copy = self.__dict__.copy()
        dict_copy.pop("_sa_instance_state", None)
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy
