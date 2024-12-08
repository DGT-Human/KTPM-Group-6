import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from .base_page import BasePage
from selenium.webdriver.support.ui import Select


# Lớp Search kế thừa từ lớp BasePage chứa các chức năng của thanh tìm kiếm
class TrackingOrder(BasePage):

    def click_option(self):
        # click vào nút tìm kiếm trong danh mục con
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[2]/div[3]/div/i").click()
        time.sleep(2)

    def click_track_order(self):
        # click vào nút tìm kiếm trong danh mục con
        self.driver.find_element(By.XPATH, "/html/body/aside/div[2]/div[2]/ul/li[4]/a").click()
        time.sleep(2)

    def check_pending_without_cancel(self):
        rows = self.driver.find_elements(By.XPATH, "//table[@class='table table-hover text-nowrap']/tbody/tr")

        for row in rows:
            # Lấy cột "Status" (cột thứ 5 trong bảng)
            status_element = row.find_element(By.XPATH, "./td[5]/span")
            status = status_element.text
            if status.lower() == "pending":
                # Lấy nút "Cancel" (nếu có) trong cột thứ 6
                try:
                    cancel_button = row.find_element(By.XPATH, "./td[6]//button[contains(text(), 'Cancel')]")
                    cancel_button_visible = cancel_button.is_displayed()
                    return cancel_button_visible  # Kiểm tra nếu nút 'Cancel' hiển thị
                except:
                    cancel_button_visible = False  # Nếu không tìm thấy nút 'Cancel'
                    return cancel_button_visible

    def check_completed_without_cancel(self):
        rows = self.driver.find_elements(By.XPATH, "//table[@class='table table-hover text-nowrap']/tbody/tr")

        for row in rows:
            # Lấy cột "Status" (cột thứ 5 trong bảng)
            status_element = row.find_element(By.XPATH, "./td[5]/span")
            status = status_element.text
            if status == "Completed":
                # Lấy nút "Cancel" (nếu có) trong cột thứ 6
                try:
                    cancel_button = row.find_element(By.XPATH, "./td[6]//button[contains(text(), 'Cancel')]")
                    cancel_button_visible = cancel_button.is_displayed()
                    return cancel_button_visible  # Kiểm tra nếu nút 'Cancel' hiển thị
                except:
                    cancel_button_visible = False  # Nếu không tìm thấy nút 'Cancel'
                    return cancel_button_visible

    def check_shipping_without_cancel(self):
        rows = self.driver.find_elements(By.XPATH, "//table[@class='table table-hover text-nowrap']/tbody/tr")

        for row in rows:
            # Lấy cột "Status" (cột thứ 5 trong bảng)
            status_element = row.find_element(By.XPATH, "./td[5]/span")
            status = status_element.text
            if status == "Shipping":
                # Lấy nút "Cancel" (nếu có) trong cột thứ 6
                try:
                    cancel_button = row.find_element(By.XPATH, "./td[6]//button[contains(text(), 'Cancel')]")
                    cancel_button_visible = cancel_button.is_displayed()
                    return cancel_button_visible  # Kiểm tra nếu nút 'Cancel' hiển thị
                except:
                    cancel_button_visible = False  # Nếu không tìm thấy nút 'Cancel'
                    return cancel_button_visible

    def click_cancel(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[2]/table/tbody/tr[1]/td[6]/form/button").click()

    def get_status(self):
        status = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[2]/table/tbody/tr[1]/td[5]/span").text
        return status

    def find_pending_order_and_cancel(self):
        # Tìm tất cả các dòng trong bảng
        rows = self.driver.find_elements(By.XPATH, "//table[@class='table table-hover text-nowrap']/tbody/tr")

        for row in rows:
            # Lấy trạng thái của đơn hàng
            status = self.get_status()

            if status == "pending":
                # Click vào nút Cancel nếu trạng thái là "pending"
                self.click_cancel()

                # Chờ một chút để hành động xảy ra
                time.sleep(2)

                # Kiểm tra xem nút Cancel có biến mất không
                # try:
                #     cancel_button = row.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[2]/table/tbody/tr[1]/td[6]/form/button")
                #     cancel_button_visible = cancel_button.is_displayed()  # Kiểm tra xem nút Cancel còn hiển thị không
                # except NoSuchElementException:
                #     cancel_button_visible = False  # Nếu không tìm thấy nút Cancel




