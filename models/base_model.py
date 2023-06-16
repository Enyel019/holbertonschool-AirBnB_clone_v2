#!/usr/bin/python3
"""Module BaseModel practice."""

import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime


Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes\
    methods for other classes."""

    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Is instantiation of base model class."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.utcnow()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def __str__(self):
        """Return a string."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.to_dict())

    def __repr__(self):
        """Return a string representation."""
        return self.__str__()

    def save(self):
        """Update the public instance attribute updated_at to current."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Create dictionary of the class  and returns in __dict__."""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in my_dict:
            del my_dict["_sa_instance_state"]
        return my_dict

    def delete(self):
        """Delete instance."""
        models.storage.delete(self)
