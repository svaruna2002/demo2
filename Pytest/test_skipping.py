import pytest
#dont want to execute any method
class Testall:
    def test_startbrowser(self):
        assert True
        print('The browser cannot be opened')

    @pytest.mark.skip
    def test_login(self):
        assert False


    @pytest.mark.xfail
    def test_logout(self):
        assert True

