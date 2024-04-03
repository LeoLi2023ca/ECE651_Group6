# conftest.py
import pytest
from my_app import test_app, db as _db  # Adjust the import based on your application structure
from my_app.models import Student, Tutor, Subject, Student_Post, ChatMessage  # Adjust the import based on your application structure

@pytest.fixture(scope='module')
def test_client():
    flask_app = test_app()  # Create an app with the testing configuration
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # This is where the testing happens!

    ctx.pop()

@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table(s)
    _db.drop_all()
    _db.create_all()

    # Insert user data
    user1 = Student(username='john_doe', nickname='john_doe', email='john@example.com', password='example')
    _db.session.add(user1)
    _db.session.commit()

    yield  # this is where the testing happens!

    _db.drop_all()
