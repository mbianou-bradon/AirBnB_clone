#!/usr/bin/python3
""" File storage classs definition """

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    obj = BaseModel(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
