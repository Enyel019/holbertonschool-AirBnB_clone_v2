#!/usr/bin/python3
"""
new engine
on db->storage
"""
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        db_user = getenv('HBNB_MYSQL_USER')
        db_password = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(db_user,
                                              db_password,
                                              db_host,
                                              db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        class_list = [State, City, User, Place, Review, Amenity]
        dict_ = {}

        if cls is None:
            for clas in class_list:
                objs = self.__session.query(clas).all()
                for obj in objs:
                    key = obj.to_dict()['__class__'] + '.' + obj.id
                    dict_[key] = obj
        else:
            cls = eval(cls)
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.to_dict()['__class__'] + '.' + obj.id
                dict_[key] = obj

        return dict_

    def new(self, obj):
        """ add object
        to currnet
        db session"""
        self.__session.add(obj)

    def save(self):
        """ stage all changes
        to session db"""
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes
        object from db session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload  from
        db to session """
        Base.metadata.create_all(self.__engine)
        session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = session()

    def close(self):
        self.__session.close()
