from PageObjects.CheckoutPage import CheckOutPage
from Utilities.BaseClass import BaseClass


class TestPage(BaseClass):




    def test_checkout(self):

        log = self.getLogger()
        checkout = CheckOutPage(self.driver)
        confirmpage = checkout.ShopButton()


        for phone in checkout.phone_List():
            if phone.text == "Blackberry":
                checkout.Blackberry().click()


        checkout.CheckoutButton()
        log.info("Entering the country name as Turkey")
        confirmpage.getCountry().send_keys("Tur")
        self.verifyLinkPresence("Turkey")


        log.info("Purchasing the phone")
        confirmpage.finalSubmit()
        textMatch = confirmpage.aLert_().text
        log.info("Text received from application is "+textMatch)
        assert ("Success!" in textMatch)