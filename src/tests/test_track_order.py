from src.data.test_data import TestData
from src.driver.driver import Driver
from src.pages.track_order import TrackingOrder
from src.pages.login_signup import LoginSignup


# Lớp TestSearch kế thừa từ lớp Driver chứa các test case
class TestTrackingOrderState(Driver):

    def test_order_state_pending(self, driver):
        driver.get("http://localhost:8000/")
        tracking = TrackingOrder(driver)
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("mini@gmail.com", "123456789")
        login.click_login()
        tracking.click_option()
        tracking.click_track_order()

        pending_rows_without_cancel = tracking.check_pending_without_cancel()
        assert pending_rows_without_cancel != False

    def test_order_state_completed(self, driver):
        driver.get("http://localhost:8000/")
        tracking = TrackingOrder(driver)
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("mini@gmail.com", "123456789")
        login.click_login()
        tracking.click_option()
        tracking.click_track_order()

        completed_rows_without_cancel = tracking.check_completed_without_cancel()
        assert completed_rows_without_cancel == False

    def test_order_state_shipping(self, driver):
        driver.get("http://localhost:8000/")
        tracking = TrackingOrder(driver)
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("mini@gmail.com", "123456789")
        login.click_login()
        tracking.click_option()
        tracking.click_track_order()

        completed_rows_without_cancel = tracking.check_shipping_without_cancel()
        assert completed_rows_without_cancel == False

    def test_click_cancel(self, driver):
        driver.get("http://localhost:8000/")
        tracking = TrackingOrder(driver)
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("mini@gmail.com", "123456789")
        login.click_login()
        tracking.click_option()
        tracking.click_track_order()
        # Kiểm tra trạng thái và nút Cancel
        tracking.find_pending_order_and_cancel()
        assert tracking.get_status() != "pending", "Status didn't change after cancel"









