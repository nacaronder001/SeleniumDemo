from selenium.webdriver.common.by import By
from PageObjects.ConfirmPage import PaymentConfirmationPage


class CheckOutPage:


    def __init__(self, driver):
        self.driver = driver



    shop = (By.XPATH, "//a[.='Shop']")
    phone_list = (By.XPATH, "//div/h4 / a")
    blackberry = (By.XPATH, "(//button[@class='btn btn-info'])[4]")
    checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkout2 = (By.CSS_SELECTOR, ".btn.btn-success")



    def ShopButton(self):
        self.driver.find_element(*CheckOutPage.shop).click()
        secondpage = PaymentConfirmationPage(self.driver)
        return secondpage

    def phone_List(self):
        return self.driver.find_elements(*CheckOutPage.phone_list)


    def Blackberry(self):
        return self.driver.find_element(*CheckOutPage.blackberry)


    def CheckoutButton(self):
        self.driver.find_element(*CheckOutPage.checkout).click()
        self.driver.find_element(*CheckOutPage.checkout2).click()
        return CheckOutPage

