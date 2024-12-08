from src.driver.driver import Driver
from src.pages.search_filter import Search_filter
from src.data.test_data import TestData


class TestSearchFilter(Driver):

    def test_search_valid(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        data = TestData.load_data('search_filter.json')['search_tests']
        search.click()
        search.search_product(data[0]['term'])
        product_names = search.data_validation_show_product()
        assert  product_names == data[0]['expected']

    def test_search_invalid(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        data = TestData.load_data('search_filter.json')['search_tests']
        search.click()
        search.search_product(data[1]['term'])
        assert search.get_message_not_found() in data[1]['expected']

    def test_search_empty(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        search.click()
        data = TestData.load_data('search_filter.json')['search_tests']
        search.search_product(data[2]['term'])

        assert search.get_message() in data[2]['expected']

    def test_search_special_characters(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        search.click()
        data = TestData.load_data('search_filter.json')['search_tests']
        search.search_product(data[2]['term2'])
        assert search.get_message() in data[2]['expected']

    def test_search_number(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        data = TestData.load_data('search_filter.json')['search_tests']
        search.click()
        search.search_product(data[3]['term'])
        product_names = search.data_validation_show_product()
        product_find = data[3]['expected']
        assert set(product_names) == set(product_find)

    def test_filter_Sort_By_Price_Default(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        search.click_menu_hg()
        data = TestData.load_data('search_filter.json')['filter_tests']
        search.click_filter()
        search.default_filter()
        product_names = search.data_validation_show_product()
        assert product_names == data[2]['excepted_default']

    def test_filter_Sort_By_Price_Low_to_High(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        search.click_menu_hg()
        data = TestData.load_data('search_filter.json')['filter_tests']
        search.click_filter()
        search.sort_low_to_high()
        product_names = search.data_validation_show_product()
        assert product_names == data[0]['excepted_Low_to_High']

    def test_filter_Sort_By_Price_High_to_Low(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        search.click_menu_hg()
        search.click_filter()
        data = TestData.load_data('search_filter.json')['filter_tests']
        search.sort_high_to_low()
        product_names = search.data_validation_show_product()
        assert product_names == data[1]['excepted_High_to_Low']

    def test_filter_by_price(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        data = TestData.load_data('search_filter.json')['filter_tests']
        search.click_menu_hg()
        search.click_filter()
        search.filter_by_price(data[3]['price_min'], data[3]['price_max'])
        product_names = search.data_validation_show_product()
        list_product_names = data[3]['excepted']
        print(product_names)
        print(list_product_names)
        assert set(product_names) == set(list_product_names)

    def test_filter_by_price_invalid(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        data = TestData.load_data('search_filter.json')['filter_tests']
        search.click_menu_hg()
        search.click_filter()
        search.filter_by_price(data[4]['price_min_invalid'], data[4]['price_max_invalid'])
        assert search.get_message_not_found() in data[4]['excepted']

    def test_filter_by_price_2_times(self, driver):
        driver.get('http://127.0.0.1:8000/')
        search = Search_filter(driver)
        data = TestData.load_data('search_filter.json')['filter_tests']
        search.click_menu_hg()
        search.click_filter()
        search.filter_by_price(data[5]['price_min_1'], data[5]['price_max_1'])
        search.click_filter()
        search.filter_by_price(data[5]['price_min_2'], data[5]['price_max_2'])
        print(search.get_message())
        print(data[5]['NotExcepted'])
        assert search.get_message_not_found() not in data[5]['NotExcepted']

