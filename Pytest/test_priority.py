import pytest
#dont want to execute any method
class Testall:
#run this method 2nd
    @pytest.mark.run(order =2)
    def test_startbrowser(self):
        assert True
        print('The browser cannot be opened')

#run this method 1st
    @pytest.mark.run(order=1)
    def test_login(self):
        assert False

#run this method 3rd
    @pytest.mark.run(order =3)
    def test_logout(self):
        assert True
