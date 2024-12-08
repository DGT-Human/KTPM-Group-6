import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select

# Lớp Search kế thừa từ lớp BasePage chứa các chức năng của thanh tìm kiếm
class Search_filter(BasePage):
    # Search
    def click(self):
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[2]/div[1]/div/i").click()

    def data_validation_show_product(self):
        time.sleep(5)
        # Tìm kiếm danh sách sản phẩm tìm thấy
        products = self.driver.find_elements(By.CSS_SELECTOR, 'a.js-name-b2')
        product_names = [product.text for product in products]
        # return danh sách sản phẩm tìm thấy
        return product_names

    def search_product(self, product_name):
        time.sleep(2)
        self.driver.find_element(By.NAME, "search").clear()
        self.driver.find_element(By.NAME, "search").send_keys(product_name)
        self.driver.find_element(By.NAME, "search").submit()

    def get_message(self):
        time.sleep(3)
        return self.driver.find_element(By.XPATH, '/html/body/div[2]').text

    def get_message_not_found(self):
        time.sleep(3)
        return self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/h1/b').text

    # Filter

    def click_menu_hg(self):
        time.sleep(3)
        menu_element = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[1]/ul/li[2]/a")
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_element).perform()
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[1]/ul/li[2]/ul/li[2]/a").click()
    def click_filter(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]").click()
        time.sleep(2)

    def default_filter(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[4]/div/div/ul/li[1]/a").click()

    def sort_low_to_high(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[4]/div/div/ul/li[2]/a").click()

    def sort_high_to_low(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[4]/div/div/ul/li[3]/a").click()

    def filter_by_price(self, min_price, max_price):
        time.sleep(3)
        script = """
            document.getElementById('priceRange').value = arguments[0];
            document.getElementById('priceRangeMax').value = arguments[1];
            document.getElementById('minPriceOutput').innerHTML = arguments[0].toLocaleString('vi-VN');
            document.getElementById('maxPriceOutput').innerHTML = arguments[1].toLocaleString('vi-VN');
            """
        self.driver.execute_script(script, min_price, max_price)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[4]/div/form/div/button").click()

    def get_price_product(self):
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, '.block2-txt .stext-105')

        # Lấy giá sản phẩm và in ra
        prices = [price.text for price in price_elements]
        print(prices)
