from src.driver.driver import Driver
from src.pages.add_to_cart import AddToCart
from src.pages.navigation import Navigation
from selenium.webdriver.common.by import By
import random


# 1 Bug
class TestAddToCart(Driver):

    def test_total_price(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)
        nav.click_gundam()
        nav.click_random_product()

        random_quantity = random.randint(1, 10)

        add.input_boundary(random_quantity)
        add.add_to_cart_successfully()
        add.click_cart()

        total_price = add.get_total_price()
        product_price = add.get_product_price()

        expected_total_price = product_price * random_quantity

        assert total_price == expected_total_price, (
            f"Total price mismatch! Expected: {expected_total_price}, Got: {total_price}"
        )
    def test_total_price_multiple_products(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)

        random_product = random.randint(1, 2)
        for i in range(random_product):
            random_quantity = random.randint(1, 7)
            nav.click_gundam()
            nav.click_random_product()
            add.input_boundary(random_quantity)
            add.add_to_cart_successfully()
        add.click_cart()

        total_price = add.get_total_price()
        item = add.get_cart_items()
        expected_total_price = 0
        product_name_expected = nav.get_added_products()
        product_name_actual = []
        for i in item:
            product_price = i["price"]
            quantity = i["quantity"]
            expected_total_price = expected_total_price + product_price * quantity
            product_name_actual.append(i["product_name"])

        assert set(product_name_actual) == set(product_name_expected)
        assert total_price == expected_total_price, (
            f"Total price mismatch! Expected: {expected_total_price}, Got: {total_price}"
        )

    def test_add_to_cart_quantity_bottom_boudary(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)
        nav.click_gundam()
        nav.click_random_product()
        add.input_boundary(0)
        add.add_to_cart_successfully()
        add.close_window()
        add.click_cart()
        element_count = add.count_elements_with_class()
        assert element_count == 0, f"Expected name not found. Got {element_count}"

    def test_add_to_cart_quantity_top_boudary(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)
        nav.click_gundam()
        nav.click_random_product()
        add.input_boundary(10000000)
        add.add_to_cart_successfully()
        add.close_window()
        add.click_cart()
        name = add.get_name()
        name_expected = nav.get_added_products()
        assert set(name) != set(name_expected)

    def test_price_sale_product_match_view_cart(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)
        nav.click_gundam()
        nav.click_random_product(True)
        add.add_to_cart_successfully()
        add.click_cart()
        product_price = add.get_product_price()
        item = add.get_cart_items()
        for i in item:
            product_price_in_cart = i["price"]
        assert product_price == product_price_in_cart

        add.click_view_cart()
        item_view_cart = add.get_product_price_in_view_cart()
        for i in item_view_cart:
            product_price_in_view_cart = i["price"]
        assert product_price == product_price_in_view_cart

    def test_remove_product_from_cart(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)

        # Click vào sản phẩm Gundam và vào chi tiết sản phẩm
        nav.click_gundam()
        nav.click_random_product()

        # Sinh số lượng ngẫu nhiên từ 1 đến 10
        random_quantity = random.randint(1, 10)

        # Thêm sản phẩm vào giỏ với số lượng ngẫu nhiên
        add.input_boundary(random_quantity)
        add.add_to_cart_successfully()
        add.click_cart()

        # Lấy giá trị tổng giá từ giỏ hàng
        total_price = add.get_total_price()
        product_price = add.get_product_price()

        # Tính tổng giá dựa trên giá sản phẩm và số lượng
        expected_total_price = product_price * random_quantity
        add.remove_product(nav.get_added_products()[0])
        add.click_cart()
        price_after_remove = total_price - expected_total_price
        total_price_after_remove = add.get_total_price()

        # Kiểm tra tổng giá từ giỏ hàng khớp với giá trị tính toán
        assert price_after_remove == total_price_after_remove, (
            f"Total price mismatch! Expected: {price_after_remove}, Got: {total_price_after_remove}"
        )

    def test_remove_product_from_cart_random_products(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)
        random_product_remove = random.randint(0, 1)

        # Click vào các sách Gundam và vào chi tiết sách Gundam
        for i in range(4):
            random_quantity = random.randint(1, 7)
            nav.click_gundam()
            nav.click_random_product()
            add.input_boundary(random_quantity)
            add.add_to_cart_successfully()

        add.click_cart()

        # Lấy giá trị tổng giá từ giỏ hàng
        add.remove_product(nav.get_added_products()[random_product_remove])
        add.click_cart()
        items = add.get_cart_items()
        price_after_remove = 0
        for item in items:
            price_after_remove = price_after_remove + item["price"] * item["quantity"]
        total_price_after_remove = add.get_total_price()

        # Kiểm tra tổng giá từ giỏ hàng khớp với giá trị tính toán
        assert price_after_remove == total_price_after_remove, (
            f"Total price mismatch! Expected: {price_after_remove}, Got: {total_price_after_remove}"
        )

    def test_update_product_quantity_random_products(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)
        random_product = random.randint(3, 5)
        for i in range(random_product):
            random_quantity = random.randint(1, 10)
            nav.click_gundam()
            nav.click_random_product()
            add.input_boundary(random_quantity)
            add.add_to_cart_successfully()
        add.click_cart()
        add.click_view_cart()

        new_quantity = random.randint(1, 10)
        random_p = random.randint(0, 1)
        add.update_product_by_name(nav.get_added_products()[random_p], new_quantity)
        random_p1 = random.randint(2, 3)
        add.update_product_by_name(nav.get_added_products()[random_p1], new_quantity)
        item_view_cart = add.get_product_price_in_view_cart()
        total_price_after_update = add.get_total_price(True)
        total_price_after_update_actual = 0
        product_name_actual = []
        for i in item_view_cart:
            total_price_after_update_actual = total_price_after_update_actual + i["price"] * i["quantity"]
            product_name_actual.append(i["product_name"])
        assert set(product_name_actual) == set(nav.get_added_products())
        assert total_price_after_update_actual == total_price_after_update

    def test_update_negative_quantity(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)
        nav.click_gundam()
        nav.click_random_product()
        random_quantity = random.randint(1, 7)
        add.input_boundary(random_quantity)
        add.add_to_cart_successfully()
        add.click_cart()
        add.click_view_cart()
        add.update_product_by_name(nav.get_added_products()[0], -1)
        assert add.get_message_input_quantity() == "Vui lòng chọn một giá trị không nhỏ hơn 1."
        add.update_product_by_name(nav.get_added_products()[0], 0)
        assert add.get_message_input_quantity() == "Vui lòng chọn một giá trị không nhỏ hơn 1."

    def test_update_out_of_max_quantity(self, driver): #BUG
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)
        nav.click_gundam()
        nav.click_random_product()
        random_quantity = random.randint(1, 7)
        add.input_boundary(random_quantity)
        add.add_to_cart_successfully()
        add.click_cart()
        add.click_view_cart()
        add.update_product_by_name(nav.get_added_products()[0], 100000)
        assert add.get_message_input_quantity() == "Vượt quá số lượng hiện có trong kho"

    def test_remove_one_product_from_view_cart(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)
        random_product = random.randint(3, 5)
        for i in range(random_product):
            random_quantity = random.randint(1, 7)
            nav.click_gundam()
            nav.click_random_product()
            add.input_boundary(random_quantity)
            add.add_to_cart_successfully()
        add.click_cart()
        add.click_view_cart()
        add.remove_product_by_name_in_view_cart(nav.get_added_products()[0])
        total_price_after_update = add.get_total_price(True)
        total_price_after_update_actual = 0
        item_view_cart = add.get_product_price_in_view_cart()
        product_name_actual = []
        product_name = nav.get_added_products()
        for i in item_view_cart:
            product_name_actual.append(i["product_name"])
            total_price_after_update_actual = total_price_after_update_actual + i["price"] * i["quantity"]
        assert total_price_after_update_actual == total_price_after_update
        assert set(product_name_actual) != set(product_name)

    def test_remove_all_products_from_view_cart(self, driver):
        driver.get("http://localhost:8000/")
        add = AddToCart(driver)
        nav = Navigation(driver)
        random_product = random.randint(3, 5)
        for i in range(random_product):
            random_quantity = random.randint(1, 7)
            nav.click_gundam()
            nav.click_random_product()
            add.input_boundary(random_quantity)
            add.add_to_cart_successfully()
        add.click_cart()
        add.click_view_cart()
        for product_name in nav.get_added_products():
            add.remove_product_by_name_in_view_cart(product_name)
        assert add.get_message_viewcart_empty() == "Không có sản phẩm nào trong giỏ hàng"



