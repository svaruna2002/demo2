import pytest
from selenium import webdriver

@pytest.fixture(scope = "class") # can use the fixture anywhere i want
def setup(self):
    print("Launching the browser for login validation") # this will execute once before every test method
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    yield
    print("closing or quitting the browser") # this will execute at the end of the execution/ will execute after every test method
    driver.close()



