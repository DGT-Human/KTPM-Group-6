import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from .base_page import BasePage


class Checkout(BasePage):

    def submit_form_guest(self, name, address, phone, email, content):
        self.driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/input").send_keys(name)
        self.driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/input").send_keys(phone)
        self.driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/input").send_keys(address)
        self.driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div[2]/div/div[2]/div[2]/div[4]/input").send_keys(email)
        self.driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div[2]/div/div[2]/div[2]/div[5]/textarea").send_keys(content)

    def button_submit(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div[2]/div/button").click()


    def close(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/i").click()
        time.sleep(2)
    def get_message_success(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]").text