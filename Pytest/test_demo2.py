import pytest
@pytest.mark.usefixtures("setup") # this will execute conftest before the class and at the end of the class
class Testnew:
    def test_Login(self,setup):
        print("Execute the login")

    def test_signoff(self,setup):
        print("logging out of the app")

    def test_tile(self,setup):
        print("title of the page")