from src.driver.driver import Driver
from src.data.test_data import TestData
from src.pages.my_account import MyAccount
from faker import Faker


class TestMyAccount(Driver):

    def test_setting_info_account(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_ex(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        faker = Faker()
        test_data = TestData.load_data('my_account.json')['info']
        phone = faker.phone_number()
        my.setting_info_account(test_data['name'], test_data['address'], phone, test_data['city'])
        assert my.get_view_name() == test_data['name']
        assert my.get_view_address() == test_data['address']
        assert my.get_view_phone() == phone

    def test_setting_info_account_name_empty(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_ex(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        faker = Faker()
        test_data = TestData.load_data('my_account.json')['info']
        phone = faker.phone_number()
        my.setting_info_account(test_data['name2'], test_data['address'], phone, test_data['city'])
        assert my.get_view_name() == test_data['name2']
        assert my.get_view_address() == test_data['address']
        assert my.get_view_phone() == phone

    def test_setting_info_account_name_too_long(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_ex(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        faker = Faker()
        test_data = TestData.load_data('my_account.json')['info']
        phone = faker.phone_number()
        my.setting_info_account(test_data['name_long'] * 255, test_data['address'], phone, test_data['city'])
        assert my.get_view_name() != test_data['name_long'] * 255
        assert my.get_view_address() == test_data['address']
        assert my.get_view_phone() == phone

    def test_setting_info_account_address_empty(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_ex(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        faker = Faker()
        test_data = TestData.load_data('my_account.json')['info']
        phone = faker.phone_number()
        my.setting_info_account(test_data['name'], test_data['address2'], phone, test_data['city'])
        assert my.get_view_name() == test_data['name']
        assert my.get_view_address() == test_data['address2']
        assert my.get_view_phone() == phone

    def test_setting_info_account_phone_empty(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_ex(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        faker = Faker()
        test_data = TestData.load_data('my_account.json')['info']
        my.setting_info_account(test_data['name'], test_data['address'], test_data['phone'], test_data['city'])
        assert my.get_view_name() == test_data['name']
        assert my.get_view_address() == test_data['address']
        assert my.get_view_phone() == test_data['phone']

    def test_setting_info_account_phone_incorrect(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_ex(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        faker = Faker()
        test_data = TestData.load_data('my_account.json')['info']
        phone = faker.phone_number()
        my.setting_info_account(test_data['name'], test_data['address'], test_data['phone2'], test_data['city'])
        assert my.get_view_name() == test_data['name']
        assert my.get_view_address() == test_data['address']
        assert my.get_view_phone() != test_data['phone2']

    def test_change_password_success(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_ex(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        test_data = TestData.load_data('my_account.json')
        password = test_data['password']
        message = test_data['message']
        my.click_change_password()
        my.form_change_password(password['current'], password['new'], password['confirm'])
        assert my.get_message_change_password() == message['success']

    def test_change_password_not_match(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_exx(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        test_data = TestData.load_data('my_account.json')
        password = test_data['password']
        message = test_data['message']
        my.click_change_password()
        my.form_change_password(password['current1'], password['new'], password['confirm2'])
        assert my.get_message_change_password() == message['failed2']

    def test_change_password_incorrect(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_exx(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        test_data = TestData.load_data('my_account.json')
        password = test_data['password']
        message = test_data['message']
        my.click_change_password()
        my.form_change_password(password['current2'], password['new'], password['confirm'])
        assert my.get_message_change_password() == message['failed']

    def test_change_password_too_short(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_exx(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        test_data = TestData.load_data('my_account.json')
        password = test_data['password']
        message = test_data['message']
        my.click_change_password()
        my.form_change_password(password['current1'], password['new_short'], password['confirm_short'])
        assert my.get_message_change_password() == message['failed1']

    def test_change_input_current_password_empty(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_exxx(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        test_data = TestData.load_data('my_account.json')
        password = test_data['password']
        message = test_data['message']
        my.click_change_password()
        my.form_change_password(password['current_empty'], password['new'], password['confirm'])
        assert my.get_message_input_current_password() == message['empty']

    def test_change_password_input_new_and_confirm_password_empty(self, driver):
        driver.get('http://127.0.0.1:8000/')
        from src.tests.test_login_signup import TestLoginSignup
        TestLoginSignup.login_exxx(self, driver)
        my = MyAccount(driver)
        my.close_menu()
        my.click_account_setting()
        test_data = TestData.load_data('my_account.json')
        password = test_data['password']
        message = test_data['message']
        my.click_change_password()
        my.form_change_password(password['current1'], password['new_empty'], password['confirm_empty'])
        assert my.get_message_input_new_password() == message['empty']
        assert my.get_message_input_confirm_password() == message['empty']
