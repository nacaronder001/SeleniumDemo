from selenium.webdriver.common.by import By



class HomePage:

    def __init__(self, driver):
        self.driver = driver


    full_name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkmark = (By.ID, "exampleCheck1")
    radiobutton = (By.ID, "inlineRadio1")
    date_of_birth = (By.NAME, "bday")
    submission = (By.CSS_SELECTOR, "input[type='submit']")
    message = (By.CSS_SELECTOR, "div[class*='alert alert-success alert-dismissible']")


    def getName(self):
        return self.driver.find_element(*HomePage.full_name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def Password(self):
        return self.driver.find_element(*HomePage.password)

    def CheckMark(self):
        return self.driver.find_element(*HomePage.checkmark)

    def radioButton(self):
        return self.driver.find_element(*HomePage.radiobutton)

    def DateofBirth(self):
        return self.driver.find_element(*HomePage.date_of_birth)

    def Submit(self):
        return self.driver.find_element(*HomePage.submission)

    def TheMessage(self):
        return self.driver.find_element(*HomePage.message)
