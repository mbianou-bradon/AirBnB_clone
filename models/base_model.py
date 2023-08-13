#!/usr/bin/python3
"""This module contains a class to serve as base for other classes"""

import uuid
from datetime import datetime
from models.engine.file_storage import storage

class BaseModel:
    """
    Base model class representing the base attributes and methods for all other models.
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            if '__class__' in kwargs:
                kwargs.pop('__class__')
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
         """
        Saves the current instance to the storage and updates the 'updated_at' attribute.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
