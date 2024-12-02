import pytest

class Testall:
    @pytest.mark.dependency()
    def test_startbrowser(self):
        assert True == True
        print('The browser cannot be opened')

    @pytest.mark.dependency(depends=['Testall:: test_start_browser'])
    def test_login(self):
        assert True == True
        print("logout successful")

#this have to be skipped because the dependenc method is failed
    @pytest.mark.dependency(depends = ['Testall: '])
    def test_logout(self):
        assert True == True
        print("logout successful")