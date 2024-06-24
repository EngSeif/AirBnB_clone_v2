#!/usr/bin/python3
"""This module defines a class to manage DBstorage for hbnb clone"""


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State, Base
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review
from models.engine.file_storage import FileStorage
from os import getenv


class DBStorage:
    """
        DBStorage Class:
        manage DBstorage for hbnb clone
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor
        """
        User = getenv('HBNB_MYSQL_USER')
        Password = getenv('HBNB_MYSQL_PWD')
        Host = getenv('HBNB_MYSQL_HOST')
        DataBase = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                            User,
                            Password,
                            Host,
                            DataBase),
                            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
            query on the current database session
        """
        session = self.__session
        class_list = [
            User,
            State,
            City,
            Amenity,
            Place,
            Review
        ]
        Result = {}
        if cls is None:
            for cls in class_list:
                objects = session.query(cls).all()
            for obj in objects:
                Key = f"{cls.__name__}.{obj.id}"
                Result[Key] = obj
        else:
            objects = session.query(cls).all()
            for obj in objects:
                Key = f"{cls.__name__}.{obj.id}"
                Result[Key] = obj
        return Result

    def new(self, obj):
        """
            add the object to the current database session
        """
        session = self.__session
        session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        session = self.__session
        session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            session = self.__session
            try:
                session.delete(obj)
            except Exception as e:
                pass

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False
                                       )
        self.__session = scoped_session(session_factory)

    def close(self):
        """
        Close session
        """
        self.__session.close()
