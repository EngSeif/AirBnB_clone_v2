#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os
import json


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        self.storage = FileStorage()
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(self.storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        ob = BaseModel()
        self.storage.new(ob)
        self.assertTrue(ob, self.storage.all().values())

def test_all(self):
    """ __objects is properly returned """
    ob = BaseModel()
    
    # Add ob to self.storage
    self.storage.new(ob)
    
    temp = self.storage.all()
    self.assertIsInstance(temp, dict)
    
    # Check if ob is in the values of temp
    self.assertIn(ob, temp.values())


    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        ob = BaseModel()
        self.storage.new(ob)
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertIn(ob.to_dict()['__class__'] + '.' + ob.id, data.keys())


    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        ob = BaseModel()
        self.storage.new(ob)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        loaded = new_storage.all()[ob.__class__.__name__ + '.' + ob.id]
        self.assertEqual(ob.id, loaded.id)

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass

        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 0)

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        new_storage = FileStorage()
        self.assertIsNone(new_storage.reload())

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertIn(new.to_dict()['__class__'] + '.' + new.id, data.keys())

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertIsInstance(self.storage.all(), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        key = new.__class__.__name__ + '.' + new.id
        self.storage.new(new)
        self.storage.save()

        keys = list(self.storage.all().keys())
        self.assertEqual(keys[0], key)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        self.assertIsInstance(self.storage, FileStorage)

    def test_delete(self):
        """ Delete an object from __objects """
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()

        key = new.__class__.__name__ + '.' + new.id
        self.assertIn(key, self.storage.all())

        self.storage.delete(new)
        self.assertNotIn(key, self.storage.all())

    def test_delete_none(self):
        """ Test delete method with None argument """
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()

        key = new.__class__.__name__ + '.' + new.id
        self.assertIn(key, self.storage.all())

        self.storage.delete()
        self.assertIn(key, self.storage.all())

    def test_delete_invalid(self):
        """ Delete an invalid object from __objects """
        # Create invalid_obj and add it to __objects
        invalid_obj = BaseModel()
        invalid_obj.id = '6c5bca5c-6400-4645-a011-a212b7e5fc06'  # Set a known id for consistency
        self.storage.new(invalid_obj)

        # Now delete invalid_obj
        self.storage.delete(invalid_obj)
        self.storage.save()
        self.assertNotIn(invalid_obj, self.storage.all())

