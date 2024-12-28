import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        PATH = Service("C:\webdrivers\chromedriver.exe")
        driver = webdriver.Chrome(service=PATH)

    elif browser_name == "firefox":
        PATH = Service("C:\webdrivers\geckodriver.exe")
        driver = webdriver.Firefox(service=PATH)

    elif browser_name == "edge":
        PATH = Service("C:\webdrivers\msedgedriver.exe")
        driver = webdriver.Edge(service=PATH)


    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()