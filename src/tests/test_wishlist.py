from src.driver.driver import Driver
from src.pages.wishlist import Wishlist
from src.pages.navigation import Navigation
from src.data.test_data import TestData

class TestWishlist(Driver):
    def test_add_to_wishlist_without_login(self, driver):
        driver.get('http://127.0.0.1:8000/')
        wishlist = Wishlist(driver)
        wishlist.click_menu_gundam()
        wishlist.add_to_wishlist(1)
        assert wishlist.get_url() == 'http://127.0.0.1:8000/users/login'

    def test_add_to_wishlist_with_login(self, driver):
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.test_login(self, driver)
        wishlist = Wishlist(driver)
        wishlist.click_close_menu()
        wishlist.click_menu_gundam()
        wishlist.add_to_wishlist(1)
        assert wishlist.get_message() == 'Product added to wishlist!'
        wishlist.click_menu()
        wishlist.click_menu_wishlist()
        product_list = wishlist.get_product_name()
        assert product_list == wishlist.get_added_products()

    def test_add_to_wishlist_multiple(self, driver):
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.test_login(self, driver)
        wishlist = Wishlist(driver)
        wishlist.click_close_menu()
        wishlist.click_menu_gundam()
        wishlist.add_to_wishlist(3)
        wishlist.click_menu()
        wishlist.click_menu_wishlist()
        product_list = wishlist.get_product_name()
        assert product_list == wishlist.get_added_products()

    def test_remove_one_product_from_wishlist(self, driver):
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.test_login(self, driver)
        wishlist = Wishlist(driver)
        wishlist.click_close_menu()
        wishlist.click_menu_gundam()
        wishlist.add_to_wishlist(3)
        wishlist.click_menu()
        wishlist.click_menu_wishlist()
        data = TestData.load_data('wishlist.json')['wishlist']
        wishlist.remove_one_product_from_wishlist(data[0]['product1'])
        product_list = wishlist.get_product_name()
        product_expected = wishlist.get_added_products()
        print(product_expected)
        print(product_list)
        assert set(product_list) == set(product_expected)
        assert wishlist.get_message() == 'Product removed from wishlist!'

    def test_remove_all_products_from_wishlist(self, driver):
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.test_login(self, driver)
        wishlist = Wishlist(driver)
        wishlist.click_close_menu()
        wishlist.click_menu_gundam()
        wishlist.add_to_wishlist(3)
        wishlist.click_menu()
        wishlist.click_menu_wishlist()
        wishlist.remove_all_products_from_wishlist()
        assert wishlist.get_product_name() == []
        assert wishlist.get_message_wishlist() == 'You have no items in your wishlist.'

    def test_add_to_wishlist_on_product_page(self, driver):
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.test_login(self, driver)
        wishlist = Wishlist(driver)
        wishlist.click_close_menu()
        wishlist.click_menu_gundam()
        nav = Navigation(driver)
        nav.click_random_product()
        wishlist.add_to_wishlist_on_product_page()
        assert wishlist.get_message() == 'Product added to wishlist!'
        wishlist.click_menu()
        wishlist.click_menu_wishlist()
        product_list = wishlist.get_product_name()
        print(product_list)
        print(nav.get_added_products())
        assert product_list == nav.get_added_products()
