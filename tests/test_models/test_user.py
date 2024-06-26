#!/usr/bin/python3
"""to easy the test use of AAA arrange act assert"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest


class test_user(unittest.TestCase):
    """
    Test the User class
    """

    def setUp(self):
        """
        Set up for tests
        """
        self.user = User(email="test@example.com",
                         password="password",
                         first_name="John",
                         last_name="Doe")

    def tearDown(self):
        """
        Tear down for tests
        """
        del self.user

    def test_initialization(self):
        """
        Test that the User instance is correctly initialized
        """
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_email_is_string(self):
        """
        Test that the email attribute is a string
        """
        self.assertIsInstance(self.user.email, str)

    def test_password_is_string(self):
        """
        Test that the password attribute is a string
        """
        self.assertIsInstance(self.user.password, str)

    def test_first_name_is_string(self):
        """
        Test that the first_name attribute is a string
        """
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_is_string(self):
        """
        Test that the last_name attribute is a string
        """
        self.assertIsInstance(self.user.last_name, str)

    def test_email_not_empty(self):
        """
        Test that the email attribute is not empty
        """
        self.assertTrue(self.user.email)

    def test_password_not_empty(self):
        """
        Test that the password attribute is not empty
        """
        self.assertTrue(self.user.password)

    def test_places_relationship(self):
        """
        Test that the places relationship exists and is empty initially
        """
        self.assertTrue(hasattr(self.user, 'places'))
        self.assertEqual(self.user.places, [])

    def test_reviews_relationship(self):
        """
        Test that the reviews relationship exists and is empty initially
        """
        self.assertTrue(hasattr(self.user, 'reviews'))
        self.assertEqual(self.user.reviews, [])
