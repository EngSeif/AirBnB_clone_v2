#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_review(self):
        """Test the time the id and everything"""
        userA = Review()
        userB = Review(**userA.to_dict())
        self.assertIsInstance(userA.id, str)
        self.assertIsInstance(userA.created_at, datetime)
        self.assertIsInstance(userA.updated_at, datetime)
        self.assertEqual(userA.updated_at, userB.updated_at)
