# def setup_module(module):
#     print("starting the server, DB, Excel, jenkins")
#
# def teardown_module(module):
#     print("clossing all the above commands")
#
# #this is at functional/method level
# def setup_function(function):
#     print("open the browser")
#
# def teardown_function(function):
#     print("close the browser")

import pytest

@pytest.fixture(scope = "module")
def setup():
    print("DB")
    yield
    print("close the DB")
@pytest.fixture(scope ="function")
def before():
    print("open the browser")
    yield
    print("close the browser")

@pytest.mark.userfixtures("setup","before")
def test_1():
    print("Login")

@pytest.mark.userfixtures("setup","before")
def test_2():
    print("logout")