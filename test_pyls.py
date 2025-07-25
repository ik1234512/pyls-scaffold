
# pytest is the module that provides us with testing helper functions.
# Mostly not needed initially, but you'll call on it in some cases.
# See documentation on pytest.

# Import the module whose procedures and functions you want to test here.
import pytest
import sys
from io import StringIO
import pyls
import os

# Note that the procedures below that are testing for things **must**
# have their names start with "test_" ... just as this file's name
# also starts with "test_". `pytest` will automatically pick up
# such functions and run them when you run `uvx pytest` from the
# command line.




'''def test_dummy():
    """
    A sample dummy test for illustration. This test will always succeed.
    """
    assert 2 == 2, "Two and two must be the same"

def test_dummy_fails():
    """
    A sample dummy test for illustration. This test will always fail.
    """
    assert 2 == 3, "Two and three must be the same. (Really?)"'''



@pytest.fixture
def capture():
    sio = StringIO()
    yield sio



@pytest.fixture
def mock_listdir_basic():
    """
    Mocks os.listdir to simulate a directory with two text files.
    """
    original_listdir = pyls.os.listdir
    pyls.os.listdir = lambda _: ["test1.txt", "test2.txt"]
    yield
    pyls.os.listdir = original_listdir



def test_basic_listing_with_capture(capture, mock_listdir_basic):
    """
    Test pyls basic output without longform or formatting.
    """
    
    old = sys.stdout
    sys.stdout = capture
    pyls.pyls(".", longform=False, formatted=False)
    sys.stdout = old    
    capture.seek(0)
    output = capture.read()

    #assert "README.md" in output,f"({output})"
    assert "test2.txt" in output

def test_pyls_sample_directory():
    """
    Test pyls on a temporary directory with sample files.
    """

    tmp_dir = "tmp_test_pyls"
    #os.mkdir(tmp_dir)
    file1 = os.path.join(tmp_dir, "file1.txt")
    file2 = os.path.join(tmp_dir, "file2.txt")
   
    old_stdout = sys.stdout
    sio = StringIO()
    sys.stdout = sio
    pyls.pyls(tmp_dir, longform=True, formatted=False)
    sys.stdout = old_stdout
    sio.seek(0)
    output = sio.read()
    assert "file1.txt" in output
    assert "file2.txt" in output
    
