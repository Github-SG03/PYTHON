import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))) #OR in terminmal exxecute the code as:export PYTHONPATH=$PYTHONPATH:$(pwd)/src then execute the pytest command for testing the test cases as like here particular testcase/function in test file :pytest tests/test_module_functions.py::test_format_file_size_returns_format_tb

from src.formatter import format_file_size


def test_format_file_size_returns_format_zero():
    assert format_file_size(0) == "0B"


def test_format_file_size_returns_format_one_byte():
    assert format_file_size(1) == "1.00 B"


def test_format_file_size_returns_format_kb():
    assert format_file_size(1024) == "1.00 KB"


def test_format_file_size_returns_format_mb():
    assert format_file_size(1024**2) == "1.00 MB"


def test_format_file_size_returns_format_gb():
    assert format_file_size(1024**3) == "1.00 GB"


def test_format_file_size_returns_format_tb():
    assert format_file_size(1024**4) == "1.00 TB"






"""                           
import pytest
from src.formatter import format_file_size
@pytest.mark.parametrize(
    "size_bytes, expected_result",
    [
        (0, "0B"),
        (1, "1.00 B"),
        (1024, "1.00 KB"),
        (1024**2, "1.00 MB"),
        (1024**3, "1.00 GB"),
        (1024**4, "1.00 TB"),
    ],
)
def test_format_file_size(size_bytes, expected_result):
    assert format_file_size(size_bytes) == expected_result


##The test_format_file_size() function now incorporates parametrization through the @pytest.mark.parametrize() decorator which lists the test cases as tuples: tuples: (sizebytes, expectedoutput)
##Pytest will run this function multiple times, once for each tuple, effectively creating separate test cases. Execute the command below to see this in action: $ pytest OR $ pytest -v(for individual test case result)

"""







"""
import pytest
from src.formatter import format_file_size


@pytest.mark.parametrize(
    "size_bytes, expected_result",
    [
        pytest.param(0, "0B", id="test_format_file_size_returns_format_zero"),
        pytest.param(1, "1.00 B", id="test_format_file_size_returns_format_one_byte"),
        pytest.param(1024, "1.00 KB", id="test_format_file_size_returns_format_kb"),
        pytest.param(1024**2, "1.00 MB", id="test_format_file_size_returns_format_mb"),
        pytest.param(1024**3, "1.00 GB", id="test_format_file_size_returns_format_gb"),
        pytest.param(1024**4, "1.00 TB", id="test_format_file_size_returns_format_tb"),
    ],
)
def test_format_file_size(size_bytes, expected_result):
    assert format_file_size(size_bytes) == expected_result

##Now, the test output will display your custom IDs, making it clearer what each test is checking.

"""



"""
from dataclasses import dataclass, field
import pytest
from src.formatter import format_file_size

@dataclass
class FileSizeTestCase:
    size_bytes: int
    expected_result: str
    id: str = field(init=False)

    def __post_init__(self):
        self.id = f"test_format_file_size_{self.size_bytes}_bytes"

test_cases = [
    FileSizeTestCase(0, "0B"),
    FileSizeTestCase(1, "1.00 B"),
    FileSizeTestCase(1024, "1.00 KB"),
    FileSizeTestCase(1024**2, "1.00 MB"),
    FileSizeTestCase(1024**3, "1.00 GB"),
    FileSizeTestCase(1024**4, "1.00 TB"),
]

@pytest.mark.parametrize("test_case", test_cases, ids=lambda tc: tc.id)
def test_format_file_size(test_case):
    assert format_file_size(test_case.size_bytes) == test_case.expected_result


##The @pytest.mark.parametrize decorator tells Pytest to run the test_format_file_size() function multiple times – once for each item in the test_cases list. In each run, the test_case parameter will be an instance of FileSizeTestCase. The ids argument in the decorator ensures that each test case in the output is clearly labelled with its generated ID.
##pytest tests/test_format_file_size.py -v to run the test cases one by one and see the result of each test case.

"""






"""
from dataclasses import dataclass, field
import pytest
from src.formatter import format_file_size


@dataclass
class FileSizeTestCase:
    size_bytes: int
    expected_result: str
    id: str = field(init=False)
    expected_error: type[Exception] = None
    error_message: str | None = None

    def __post_init__(self):
        self.id = f"test_format_file_size_{self.size_bytes}_bytes"


test_cases = [
    FileSizeTestCase(0, "0B"),
    FileSizeTestCase(1, "1.00 B"),
    FileSizeTestCase(1024, "1.00 KB"),
    FileSizeTestCase(1024**2, "1.00 MB"),
    FileSizeTestCase(1024**3, "1.00 GB"),
    FileSizeTestCase(1024**4, "1.00 TB"),
    FileSizeTestCase(
        -1, "", ValueError, "Size cannot be negative"
    ),  # Test case expecting an error
]


@pytest.mark.parametrize("test_case", test_cases, ids=lambda tc: tc.id)
def test_format_file_size(test_case):
    if test_case.expected_error:
        with pytest.raises(test_case.expected_error, match=test_case.error_message):
            format_file_size(test_case.size_bytes)

    else:
        assert format_file_size(test_case.size_bytes) == test_case.expected_result


##This code passes a negative input (-1) to format_file_size() and the pytest.raises() context manager verifies if a ValueError with the message "Size cannot be negative" is raised.
##Here, two fields were added to the FileSizeTestCase class: expected_error, and error_message. These signal if an error is expected and its message.
The new test case is then supplied an input of -1 to trigger the error, and the expected_error and error_message fields are supplied accordingly.
Finally, in the test_format_file_size() function, pytest.raises() checks the exception type and the error message. If no error is expected, assert ensures that the formatted output matches the expected result.
Upon saving and running the test, you'll see that it passes, confirming that the ValueError exception was raised:

"""






