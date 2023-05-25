#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        """Comment."""
        db_user = getenv('HBNB_MYSQL_USER')
        db_pass = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(db_user, db_pass, db_host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        def all(self, cls=None):
            """Query on the current database session."""
            classes = [User, State, City, Amenity, Place, Review]
            dict_ = {}

            if cls is None:
                for cls in classes:
                    objs = self.__session.query(cls).all()
                    for obj in objs:
                        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                        dict_[key] = obj
            else:
                cls = eval(cls)
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                dict_[key] = obj

            return dict_

        def new(self, obj):
            """Add the object to the current database session."""
            if obj:
                self.__session.add(obj)

        def save(self):
            """Commit all changes of the current database session."""
            self.__session.commit()

        def delete(self, obj=None):
            """Delete from the current database session."""
            if obj:
                self.__session.delete(obj)

        def reload(self):
            """Create all tables in the database."""
            Base.metadata.create_all(self.__engine)
            session = scoped_session(sessionmaker(bind=self.__engine,
                                                  expire_on_commit=False))
            self.__session = session()
