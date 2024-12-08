import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Wishlist(BasePage):
    def click_menu_gundam(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[1]/ul/li[2]/a").click()

    def add_to_wishlist(self, quantity):
        if quantity < 1:
            print("Số lượng phải lớn hơn hoặc bằng 1.")
            return

        # Biến đếm số lượng sản phẩm đã thêm vào wishlist
        added_to_wishlist = 0

        while added_to_wishlist < quantity:
            try:
                # Tìm danh sách các nút "Add to Wishlist"
                wishlist_buttons = self.driver.find_elements(By.CSS_SELECTOR, "a.btn-addwish-b2")

                # Đảm bảo danh sách có đủ các sản phẩm để thêm
                if len(wishlist_buttons) <= added_to_wishlist:
                    print("Không còn sản phẩm nào để thêm vào wishlist.")
                    break

                # Lấy nút của sản phẩm tiếp theo
                button = wishlist_buttons[added_to_wishlist]

                # Lấy tên sản phẩm trước khi nhấn vào nút "Add to Wishlist"
                product_name = self.driver.find_elements(By.CSS_SELECTOR, '.stext-104.cl4.hov-cl1.trans-04.js-name-b2.p-b-6')[added_to_wishlist].text

                # Di chuyển tới nút và click
                ActionChains(self.driver).move_to_element(button).click().perform()

                # Đợi một chút để đảm bảo sản phẩm đã được thêm vào wishlist
                time.sleep(2)

                # Kiểm tra xem có thông báo thành công hay sự thay đổi nào để xác nhận sản phẩm đã được thêm vào wishlist
                success_message = self.driver.find_elements(By.XPATH, "/html/body/div[2]")  # Thay đổi XPath nếu cần

                if success_message:
                    # Nếu thông báo thành công, thêm tên sản phẩm vào danh sách
                    self.added_products.append(product_name)
                    print(f"Đã thêm sản phẩm {product_name} vào wishlist.")
                else:
                    print(f"Sản phẩm {product_name} chưa được thêm vào wishlist.")

                added_to_wishlist += 1
                print(f"Đã thêm sản phẩm thứ {added_to_wishlist} vào wishlist.")
                time.sleep(2)  # Đợi một chút giữa các lần click để tránh lỗi

            except Exception as e:
                print(f"Lỗi khi thêm sản phẩm thứ {added_to_wishlist + 1} vào wishlist: {str(e)}")
                time.sleep(3)  # Đợi và thử lại nếu có lỗi

    def add_to_wishlist_on_product_page(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/section/div[1]/div[1]/div[2]/div/div[2]/div/a/i").click()

    def get_added_products(self):
        return self.added_products

    def get_url(self):
        return self.driver.current_url

    def get_message(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[2]').text

    def click_menu(self):
        self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[2]/div[3]/div/i").click()

    def click_menu_wishlist(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/aside/div[2]/div[2]/ul/li[2]/a").click()

    def click_close_menu(self):
        self.driver.find_element(By.XPATH, "/html/body/aside/div[2]/div[1]/div/i").click()

    def get_product_name(self):
        product_names = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr td a")

        # In danh sách tên sản phẩm
        product_list = [product.text for product in product_names]
        return product_list

    def remove_one_product_from_wishlist(self, product_name):
        try:
            # Tìm hàng chứa sản phẩm dựa trên tên sản phẩm
            rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
            for row in rows:
                name_element = row.find_element(By.CSS_SELECTOR, "td a")
                name = name_element.text.strip()
                if name == product_name:
                    # Tìm nút "Remove" trong hàng này và click vào nó
                    remove_button = row.find_element(By.CSS_SELECTOR, "button.btn-danger")
                    ActionChains(self.driver).move_to_element(remove_button).click().perform()
                    self.added_products.remove(product_name)
                    print(f"Đã xóa sản phẩm '{product_name}' khỏi wishlist.")
                    time.sleep(2)
                    return
            print(f"Sản phẩm '{product_name}' không có trong wishlist.")
        except Exception as e:
            print(f"Lỗi khi xóa sản phẩm: {str(e)}")

    def remove_all_products_from_wishlist(self):
        try:
            while True:
                time.sleep(2)

                # Lấy danh sách các nút "Remove"
                remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, "form button.btn-danger")

                if not remove_buttons:
                    print("Wishlist đã trống.")
                    break

                # Nhấp vào nút đầu tiên trong danh sách
                button = remove_buttons[0]
                try:
                    ActionChains(self.driver).move_to_element(button).perform()
                    button.click()
                    print("Đã xóa một sản phẩm khỏi wishlist.")

                    # Chờ DOM cập nhật sau khi xóa
                    time.sleep(3)
                except Exception as e:
                    print(f"Lỗi khi xóa sản phẩm: {str(e)}")
                    break

            print("Đã xóa tất cả sản phẩm khỏi wishlist.")
        except Exception as e:
            print(f"Lỗi tổng quát khi xóa tất cả sản phẩm: {str(e)}")

    def get_message_wishlist(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[3]/h2').text