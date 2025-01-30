
import pytest

@pytest.fixture()
def welcome_message():
    """Return a welcome message."""
    return "Welcome to our application!"

def test_welcome_message(welcome_message):
    """Test if the fixture returns the correct welcome message."""
    assert welcome_message == "Welcome to our application!"




##The @pytest.fixture() decorator defines a fixture in Pytest. Such fixtures, like welcome_message(), can execute setup tasks and deliver data to test functions. When a test function lists a fixture by name as a parameter, Pytest automatically invokes the fixture function before running the test function.
##Execute these tests by running the following command:pytest tests/test_format_file_size_with_fixtures.py

