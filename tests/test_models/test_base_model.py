#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
from unittest.mock import patch
import json
import os


class test_basemodel(unittest.TestCase):
    """
    Class To Test BaseModel Class
    """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        self.model = BaseModel()
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass
        del self.model

    def test_unique_id(self):
        """
        Test If the Id is Unique
        """
        self.assertIsInstance(self.model.id, str)
        self.assertTrue(UUID(self.model.id))

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test the __str__ method of the BaseModel class"""
        val = self.model
        dict_copy = val.__dict__.copy()
        dict_copy.pop('_sa_instance_state', None)
        expected_str = '[{}] ({}) {}'.format(val.__class__.__name__, val.id, dict_copy)
        self.assertEqual(str(val), expected_str)

    def test_todict(self):
        """ """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(
            model_dict["created_at"], self.model.created_at.isoformat()
        )
        self.assertEqual(
            model_dict["updated_at"], self.model.updated_at.isoformat()
        )

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """
        Test BaseModel initialization with arbitrary kwargs
        """
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertEqual(new.Name, 'test')

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        self.assertEqual(type(self.model.updated_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(self.model.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertEqual(new.created_at, new.updated_at)

    def test_delete(self):
        """
        Test the delete method
        """
        with patch('models.storage') as mock_storage:
            self.model.delete()
            mock_storage.delete.assert_called_with(self.model)
