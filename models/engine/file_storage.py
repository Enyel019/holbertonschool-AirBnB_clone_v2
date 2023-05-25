#!/usr/bin/python3
"""This is the file storage class for AirBnB."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary."""
        if cls is None:
            return self.__objects
        else:
            n_d = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    n_d[key] = value
            return n_d

    def new(self, obj):
        """Set __object to given obj."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize the file path to JSON file path."""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Serialize the file path to JSON file path."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete an object object from storage."""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]
            self.save()
