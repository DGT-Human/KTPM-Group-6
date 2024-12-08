import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select

# Lớp Search kế thừa từ lớp BasePage chứa các chức năng của thanh tìm kiếm
class LoginSignup(BasePage):
  # Phương thức tìm kiếm sản phẩm trong danh mục con
    def click_menu(self):
        # click vào nút tìm kiếm trong danh mục con
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[2]/div[3]/div/i").click()
        time.sleep(2)

    def click_account(self):
        self.driver.find_element(By.XPATH, "/html/body/aside/div[2]/div[2]/ul/li[3]/a").click()
        time.sleep(2)

    def fill_name_and_password(self, username, password):
        self.driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[1]/input").send_keys(username)
        self.driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[2]/input").send_keys(password)

    def fill_email_name_and_password(self,name, username, password, confirm_pass):
        self.driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[1]/input").send_keys(name)
        self.driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[2]/input").send_keys(username)
        self.driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[3]/input").send_keys(password)
        self.driver.find_element(By.XPATH, "//html/body/section/div/div[1]/form/div[4]/input").send_keys(confirm_pass)


    def click_signup(self):
        self.driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[5]/button").click()
        time.sleep(2)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//html/body/section/div/div[1]/form/div[4]/button").click()
        time.sleep(2)

    def get_name(self):
        displayed_name = self.driver.find_element(By.XPATH, "/html/body/aside/div[2]/div[2]/ul/li[3]/a[1]").text
        return displayed_name

    def click_logout(self):
        self.driver.find_element(By.XPATH, "/html/body/aside/div[2]/div[2]/ul/li[3]/a[2]").click()
        time.sleep(2)

    def get_alert_message(self):
        alert_div = self.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger")

        # Lấy nội dung văn bản của thẻ `div`
        alert_text = alert_div.text
        return alert_text

    def get_alert_success_message(self):
        alert_div = self.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success")
        # Lấy nội dung văn bản của thẻ `div`
        alert_text = alert_div.text
        return alert_text

    def click_register(self):
        self.driver.find_element(By.XPATH, "/html/body/section/div/div[1]/div/span/a").click()
        time.sleep(2)

    def click_forgot_password(self):
        self.driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[3]/a").click()
        time.sleep(2)
    def fill_email(self, email):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/form/div/input").send_keys(email)

    def click_confirm(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/form/button").click()
        time.sleep(2)

    def fill_password(self, password, confirm_pass):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/input").send_keys(password)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/form/div[2]/input").send_keys(confirm_pass)

    def click_change_password(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/form/button").click()
        time.sleep(2)
