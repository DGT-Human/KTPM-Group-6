from src.driver.driver import Driver
from src.pages.checkout import Checkout
from src.pages.add_to_cart import AddToCart
from src.data.test_data import TestData
from src.pages.my_account import MyAccount
from faker import Faker


class TestCheckout(Driver):
    def test_checkout_guest_success(self, driver):
        driver.get('http://127.0.0.1:8000/')
        test_data = TestData.load_data('checkout.json')
        message = test_data['message']
        check = Checkout(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        add.click_view_cart()
        check.submit_form_guest(faker.name(), faker.address(), faker.phone_number(), faker.email(), '')
        check.button_submit()
        assert check.get_message_success() == message['success']

    def test_checkout_address_invalid(self, driver):
        driver.get('http://127.0.0.1:8000/')
        test_data = TestData.load_data('checkout.json')
        guest_invalid = test_data['guest_invalid']
        message = test_data['message']
        check = Checkout(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        add.click_view_cart()
        check.submit_form_guest(faker.name(), guest_invalid['address'], faker.phone_number(),
                                faker.email(), '')
        check.button_submit()
        assert check.get_message_success() == message['failed']

    def test_checkout_phone_invalid(self, driver):
        driver.get('http://127.0.0.1:8000/')
        test_data = TestData.load_data('checkout.json')
        guest_invalid = test_data['guest_invalid']
        message = test_data['message']
        check = Checkout(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        add.click_view_cart()
        check.submit_form_guest(faker.name(), faker.address(), guest_invalid['phone'], faker.email(), '')
        check.button_submit()
        assert check.get_message_success() == message['failed']

    def test_checkout_email_invalid(self, driver):
        driver.get('http://127.0.0.1:8000/')
        test_data = TestData.load_data('checkout.json')
        guest_invalid = test_data['guest_invalid']
        message = test_data['message']
        check = Checkout(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        add.click_view_cart()
        check.submit_form_guest(faker.name(), faker.address(), faker.phone_number(), guest_invalid['email'], '')
        check.button_submit()
        assert check.get_message_success() == message['failed']

    def test_checkout_email_incorrect(self, driver):
        driver.get('http://127.0.0.1:8000/')
        test_data = TestData.load_data('checkout.json')
        guest_fail = test_data['guest_fail']
        message = test_data['message']
        check = Checkout(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        add.click_view_cart()
        check.submit_form_guest(faker.name(), faker.address(), faker.phone_number(), guest_fail['email'], '')
        check.button_submit()
        assert check.get_message_success() == message['failed']

    def test_checkout_phone_incorrect(self, driver):
        driver.get('http://127.0.0.1:8000/')
        test_data = TestData.load_data('checkout.json')
        guest_fail = test_data['guest_fail']
        message = test_data['message']
        check = Checkout(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        add.click_view_cart()
        check.submit_form_guest(faker.name(), faker.address(), guest_fail['phone'], faker.email(), '')
        check.button_submit()
        assert check.get_message_success() == message['failed']

    def test_checkout_name_invalid(self, driver):
        driver.get('http://127.0.0.1:8000/')
        test_data = TestData.load_data('checkout.json')
        guest_invalid = test_data['guest_invalid']
        message = test_data['message']
        check = Checkout(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        add.click_view_cart()
        check.submit_form_guest(guest_invalid['name'], faker.address(), faker.phone_number(), faker.email(), '')
        check.button_submit()
        assert check.get_message_success() == message['failed']

    def test_checkout_name_too_long(self, driver):
        driver.get('http://127.0.0.1:8000/')
        test_data = TestData.load_data('checkout.json')
        guest_invalid = test_data['guest_invalid']
        message = test_data['message']
        check = Checkout(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        add.click_view_cart()
        check.submit_form_guest(guest_invalid['name2'] * 255, faker.address(), faker.phone_number(), faker.email(), '')
        check.button_submit()
        assert check.get_message_success() == message['failed']

    def test_checkout_account_success(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.test_login(self, driver)
        check = Checkout(driver)
        my = MyAccount(driver)
        add = AddToCart(driver)
        faker = Faker()
        test_data = TestData.load_data('checkout.json')
        message = test_data['message']
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        check.close()
        my.click_account_setting()
        my.setting_info_account(faker.name(), faker.address(), faker.phone_number(), 'Hà Nội')
        add.click_cart()
        add.click_view_cart()
        check.button_submit()
        assert check.get_message_success() == message['success']

    def test_checkout_account_invalid_name(self, driver):
        driver.get('http://127.0.0.1:8000/')
        check = Checkout(driver)
        my = MyAccount(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.test_login(self, driver)
        invalid = TestData.load_data('checkout.json')['guest_invalid']
        message = TestData.load_data('checkout.json')['message']['failed']
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        check.close()
        my.click_account_setting()
        my.setting_info_account(invalid['name'], faker.address(), faker.phone_number(), 'Hà Nội')
        add.click_cart()
        add.click_view_cart()
        check.button_submit()
        assert check.get_message_success() == message

    def test_checkout_account_invalid_address(self, driver):
        driver.get('http://127.0.0.1:8000/')
        check = Checkout(driver)
        my = MyAccount(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.test_login(self, driver)
        invalid = TestData.load_data('checkout.json')['guest_invalid']
        message = TestData.load_data('checkout.json')['message']['failed']
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        check.close()
        my.click_account_setting()
        my.setting_info_account(invalid['name2'], invalid['address'], faker.phone_number(), 'Hà Nội')
        add.click_cart()
        add.click_view_cart()
        check.button_submit()
        assert check.get_message_success() == message

    def test_checkout_account_invalid_phone(self, driver):
        driver.get('http://127.0.0.1:8000/')
        check = Checkout(driver)
        my = MyAccount(driver)
        add = AddToCart(driver)
        faker = Faker()
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.test_login(self, driver)
        invalid = TestData.load_data('checkout.json')['guest_invalid']
        message = TestData.load_data('checkout.json')['message']['failed']
        from src.tests.test_add_to_cart import TestAddToCart
        TestAddToCart.test_total_price_multiple_products(self, driver)
        check.close()
        my.click_account_setting()
        my.setting_info_account(invalid['name2'], faker.address(), invalid['phone'], 'Hà Nội')
        add.click_cart()
        add.click_view_cart()
        check.button_submit()
        assert check.get_message_success() == message




