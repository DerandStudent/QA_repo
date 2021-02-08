import unittest
from flask.helpers import url_for
from flask_testing import TestCase

# import the neccessary modules from the app.py file
from app import app, db, Todo

# create a test case that inherits fromn the testBase class


class TestBase(TestCase):
    def create_app(self):
        # cant use the inbuilt database
        # create a new sqlite temp database to use so that we dont affect the live one
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                          SECRET_KEY='testkey',
                          DEBUG=True)
        # will return the new configs
        return app

    # this always happens as it is the setup test method
    # will happen before every test
    def setUp(self):
        # the drop all function isn't neccesssary as we are using an sqlite database and so it wont affect anything
        # this would be neccessary if we were using an inbuilt database
        db.create_all()

    # after the teats are finished

    def tearDown(self):
        db.sessions.remove()
        db.drop_all()


class TestAccess(TestBase):
    # check that the page access was successful
    def test_access_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


class TestAdd(TestBase):

    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data=dict(todolist="mow the lawn"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
