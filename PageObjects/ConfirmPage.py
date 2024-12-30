from selenium.webdriver.common.by import By



class PaymentConfirmationPage:


    def __init__(self, driver):
        self.driver = driver


    country = (By.XPATH, "//input[@id='country']")
    turkey =  (By.LINK_TEXT, "Turkey")
    submit = (By.XPATH, "//input[@type='submit']")





    def getCountry(self):
        return self.driver.find_element(*PaymentConfirmationPage.country)



    def finalSubmit(self):
        self.driver.find_element(*PaymentConfirmationPage.turkey).click()
        self.driver.find_element(*PaymentConfirmationPage.submit).click()
        return PaymentConfirmationPage


    def aLert_(self):
        return self.driver.find_element(By.CLASS_NAME, "alert-success")











