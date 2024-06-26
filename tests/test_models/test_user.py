#!/usr/bin/python3
"""to easy the test use of AAA arrange act assert"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_email_and_password_not_same(self):
        """Tests that email and password are not the same string."""
        """Arrange"""
        user = User(email="test@example.com", password="secret123")
        self.assertNotEqual(user.email, user.password)

    def test_email_contains_at(self):
        """Tests that email contains the '@'"""
        user = User(email="test@example.com", password="secret123")
        self.assertIn('@', user.email)

    def test_password_at_least_four_chars(self):
        """Tests that password has at least 4 characters."""
        user = User(email="test@example.com", password="secret"
        self.assertGreaterEqual(len(user.password), 4)

    def test_null_email_raises_ValueError(self):
        """Tests that creating a User with an empty email raises a ValueError."""
        with self.assertRaises(ValueError):
            user = User(email="", password="secret123")
        """"no act or assert needed"""
