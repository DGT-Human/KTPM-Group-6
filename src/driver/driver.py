import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

class Driver():
    # @pytest.fixture(scope="function")
    # def driver(self): # msedgedriver
    #     options = webdriver.EdgeOptions()
    #     driver = webdriver.Edge(options=options)
    #     driver.maximize_window()
    #     yield driver
    #     driver.quit()

    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()