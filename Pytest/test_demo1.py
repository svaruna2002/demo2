#Pytest

# class TestDemo:
#     def test_Demo1(self):
#         print("This is my first pytest class")
#
#     def test_Demo2(self):
#         print("This is the second method")

import pytest
# creating the first decorator
@pytest.fixture() # can use the fixture anywhere i want
def setup(self):
    print("Launching the browser for login validation") # this will execute once before every test method
    yield
    print("closing or quitting the browser") # this will execute at the end of the execution

