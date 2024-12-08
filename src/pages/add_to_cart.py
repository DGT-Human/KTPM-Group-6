import time
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from .base_page import BasePage


# Lớp Search kế thừa từ lớp BasePage chứa các chức năng của thanh tìm kiếm
class AddToCart(BasePage):

    def add_to_cart_successfully(self):
        self.driver.find_element(By.XPATH, "/html/body/section/div[1]/div[1]/div[2]/div/div[1]/div/form/button").click()
        time.sleep(2)

    def click_cart(self):
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[2]/div[2]/div").click()
        time.sleep(2)

    def get_name(self):
        # CSS selector để lấy tất cả các tên sản phẩm trong danh sách giỏ hàng
        product_name_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                          ".header-cart-wrapitem .header-cart-item-txt .header-cart-item-name")

        # Duyệt qua các phần tử và lấy tên sản phẩm
        product_names = [product.text.strip() for product in product_name_elements]

        return product_names

    def count_elements_with_class(self):
        try:
            # Tìm tất cả các phần tử với class cụ thể
            elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-cart-item-name.m-b-18.hov-cl1.trans-04")
            return len(elements)  # Trả về số lượng phần tử tìm thấy
        except Exception as e:
            print(f"Error: {e}")
            return 0

    def input_boundary(self, quantity):
        time.sleep(2)
        quantity_input = self.driver.find_element(By.XPATH,
                                                  "/html/body/section/div[1]/div[1]/div[2]/div/div[1]/div/form/div/input")
        quantity_input.clear()  # Xóa giá trị cũ
        # Nhập số lượng mới
        quantity_input.send_keys(quantity)

    def close_window(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[5]/div/div[4]/div/button").click()

    def get_total_price(self, view_cart_checkout=False):
        if view_cart_checkout:
            total_price_text = self.driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div[2]/div/div[1]/div[2]/span").text
            return int(total_price_text.replace(".", "").replace("đ", ""))
        else:
            # Tìm phần tử chứa tổng giá bằng XPath
            total_price_text = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]").text

            # Sử dụng regex để tìm số trong văn bản (loại bỏ chữ và định dạng)
            match = re.search(r"[\d.]+", total_price_text)
            if match:
                # Loại bỏ dấu chấm và chuyển đổi thành số nguyên
                return int(match.group(0).replace(".", ""))
            else:
                raise ValueError("Không tìm thấy tổng giá trong văn bản.")

    def get_product_price(self):
        # Tìm phần tử chứa giá bằng XPath
        product_price_text = self.driver.find_element(By.XPATH,
                                                      "/html/body/section/div[1]/div[1]/div[2]/div/span").text

        # Tìm "Đang Sale" trong chuỗi và lấy số tương ứng
        match = re.search(r"Đang Sale: ([\d,]+)đ", product_price_text)
        if match:
            # Trả về giá trị số, loại bỏ dấu phẩy
            return int(match.group(1).replace(",", ""))
        else:
            return int(product_price_text.replace(",", "").replace("đ", ""))

    def get_cart_items(self):
        cart_items = []

        # Tìm tất cả các sản phẩm trong giỏ hàng
        items = self.driver.find_elements(By.CSS_SELECTOR, "ul.header-cart-wrapitem li.header-cart-item")

        for item in items:
            product_name = item.find_element(By.CSS_SELECTOR, "a.header-cart-item-name").text
            # Lấy thông tin số lượng và giá
            product_info = item.find_element(By.CSS_SELECTOR, "span.header-cart-item-info").text
            quantity, price = product_info.split(' x ')  # Tách số lượng và giá

            # Lấy giá trị số lượng và giá
            quantity = int(quantity.strip())
            price = int(price.replace(".", "").replace("đ", ""))  # Làm sạch giá trị và loại bỏ dấu phân cách

            # Lưu vào danh sách
            cart_items.append({
                "product_name": product_name,
                "quantity": quantity,
                "price": price
            })

        return cart_items


    def remove_product(self, product_name):
        items = self.driver.find_elements(By.CSS_SELECTOR, ".header-cart-item")

        for item in items:
            product_info = item.find_element(By.CSS_SELECTOR, ".header-cart-item-name").text

            if product_info == product_name:
                remove_button = item.find_element(By.CSS_SELECTOR, 'a[href*="remove-cart"]')
                actions = ActionChains(self.driver)
                actions.move_to_element(remove_button).click().perform()
                time.sleep(3)
                break

    def click_view_cart(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/a[1]").click()
        time.sleep(2)

    def update_product_by_name(self, product_name, new_quantity):
        # Tìm tất cả các dòng trong tbody
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr.table_row")

        for row in rows:
            # Lấy tên sản phẩm trong cột thứ 2
            product_name_in_row = row.find_element(By.CSS_SELECTOR, "td.column-2").text

            # Kiểm tra nếu tên sản phẩm khớp
            if product_name_in_row == product_name:
                # Cập nhật số lượng sản phẩm
                quantity_input = row.find_element(By.CSS_SELECTOR, "input.num-product")
                quantity_input.clear()  # Xóa giá trị cũ
                quantity_input.send_keys(str(new_quantity))

        self.driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div[1]/div/div[2]/input[1]").click()

    def remove_product_by_name_in_view_cart(self, product_name):
        time.sleep(2)
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr.table_row")

        for row in rows:
            product_name_in_row = row.find_element(By.CSS_SELECTOR, "td.column-2").text

            if product_name_in_row == product_name:
                for product_name_in_row in self.added_products:
                    self.added_products.remove(product_name_in_row)
                remove_button = row.find_element(By.CSS_SELECTOR, "a.btn-danger")
                self.scroll_to_element(remove_button)
                ActionChains(self.driver).move_to_element(remove_button).click().perform()

    def get_product_price_in_view_cart(self):
        # Tìm tất cả các dòng trong tbody
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr.table_row")
        cart_item = []
        for row in rows:
            product_name = row.find_element(By.CSS_SELECTOR, "td.column-2").text
            # Lấy tên sản phẩm trong cotland 2
            product_price = row.find_element(By.CSS_SELECTOR, "td.column-3").text
            quantity = row.find_element(By.CSS_SELECTOR, "td.column-4 input").get_attribute('value')
            quantity = int(quantity.strip())
            price = int(product_price.replace(".", "").replace("đ", ""))
            cart_item.append({
                "product_name": product_name,
                "quantity": quantity,
                "price": price
            })
        return cart_item

    def get_message_viewcart_empty(self):
        time.sleep(2)
        return self.driver.find_element(By.XPATH, "/html/body/form/div/div[2]/h2").text

    def get_message_input_quantity(self):
        input_element = self.driver.find_element(By.XPATH, "//input[contains(@class, 'num-product')]")
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", input_element)
        return validation_message





