import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class MyAccount(BasePage):

    def setting_info_account(self, name, address, phone, city):
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form/div[1]/div/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form/div[1]/div/input").send_keys(name)
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form/div[3]/div/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form/div[3]/div/input").send_keys(phone)
        self.scroll_to_element(self.driver.find_element(By.ID, "inputExperience"))
        self.driver.find_element(By.ID, "inputExperience").clear()
        self.driver.find_element(By.ID, "inputExperience").send_keys(address)
        dropdown = Select(self.driver.find_element(By.ID, 'city'))

        # Chọn thành phố "Hồ Chí Minh" theo visible text
        dropdown.select_by_visible_text(city)

        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form/div[6]/div/button[1]").click()


    def click_account_setting(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[2]/div[3]/div/i").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/aside/div[2]/div[2]/ul/li[3]/a[1]").click()
        time.sleep(2)

    def close_menu(self):
        self.driver.find_element(By.XPATH, "/html/body/aside/div[2]/div[1]/div/i").click()
        time.sleep(2)

    def get_view_phone(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[4]/p[2]").text

    def get_view_name(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div/h3").text

    def get_view_address(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[4]/p[3]").text

    def click_change_password(self):
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form/div[6]/div/button[2]"))
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form/div[6]/div/button[2]").click()
        time.sleep(2)

    def form_change_password(self, old_password, new_password, confirm_password):
        self.driver.find_element(By.ID, "currentPassword").clear()
        self.driver.find_element(By.ID, "currentPassword").send_keys(old_password)
        self.driver.find_element(By.ID, "newPassword").clear()
        self.driver.find_element(By.ID, "newPassword").send_keys(new_password)
        self.driver.find_element(By.ID, "confirmPassword").clear()
        self.driver.find_element(By.ID, "confirmPassword").send_keys(confirm_password)
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/form/div[2]/button[2]").click()
        time.sleep(3)

    def get_message_change_password(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[3]").text

    def get_message_input_new_password(self):
        input_element = self.driver.find_element(By.XPATH, "//input[contains(@ID, 'newPassword')]")
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", input_element)
        return validation_message

    def get_message_input_confirm_password(self):
        input_element = self.driver.find_element(By.XPATH, "//input[contains(@ID, 'confirmPassword')]")
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", input_element)
        return validation_message

    def get_message_input_current_password(self):
        input_element = self.driver.find_element(By.XPATH, "//input[contains(@ID, 'currentPassword')]")
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", input_element)
        return validation_message