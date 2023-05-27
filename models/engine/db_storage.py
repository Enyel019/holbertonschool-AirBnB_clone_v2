#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review


class DBStorage:
    """The class DBStorage is defined for database storage in Python."""

    __engine = None
    __session = None

    def __init__(self):
        """
        This is the constructor method for a Python class.
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user,
                                                 password, host, database),
            pool_pre_ping=True
        )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        session = self.__session
        classes = [User, State, City, Amenity, Place, Review]

        if cls:
            query = session.query(cls).all()
        else:
            query = []
            for cls in classes:
                query += session.query(cls).all()

        objects = {}
        for obj in query:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects[key] = obj

        return objects

    def new(self, obj):
        """
        The function "new" takes in an object as a parameter.

        :param obj: The "obj" parameter in the "new" method is typically used to create a new instance
        of a class. It represents the object that is being created and initialized. The "self"
        parameter, on the other hand, refers to the instance of the class that the method is being
        called on
        """
        self.__session.add(obj)

    def save(self):
        """
        The function "save" is defined, but its implementation is not shown.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        The function "delete" takes an optional argument "obj" and does not have any implementation
        provided in the code snippet.

        :param obj: The "obj" parameter in the "delete" method is an optional argument that represents
        the object to be deleted. If no argument is provided, the method will delete the entire object
        that the method is called on. If an argument is provided, the method will delete only that
        specific object
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        The function "reload" is not defined and therefore cannot be summarized.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
