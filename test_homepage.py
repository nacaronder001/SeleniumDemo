import pytest
from homepageData import HomePage
from PageObjects.homepageData import HomePage

@pytest.mark.usefixtures("setup")
class TestHomePage:


    def test_formSubmission(self, getData):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["fullname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.Password().send_keys(getData["password"])
        homepage.CheckMark().click()
        homepage.radioButton().click()
        homepage.DateofBirth().send_keys("03/18/1996")
        homepage.Submit().click()
        message = "Success!"
        assert message in homepage.TheMessage().text








    @pytest.fixture(params=[{"fullname": "Onder Nacar", "email": "nacaronder001@gmail.com", "password": "1234567890"}])
    def getData(self, request):
        return request.param

