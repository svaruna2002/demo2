import pytest
#dont want to execute any method
class Testall:

    @pytest.mark.sanity
    def test_startbrowser(self):
        assert True
        print('The browser cannot be opened')

    @pytest.mark.regression
    def test_login(self):
        assert False

    @pytest.mark.sanity
    def test_logout(self):
        assert True

    @pytest.mark.regression
    def test_logout(self):
        assert True