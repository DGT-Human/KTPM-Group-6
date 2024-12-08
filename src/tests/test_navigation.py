from src.data.test_data import TestData
from src.driver.driver import Driver
from src.pages.navigation import Navigation



# Lớp TestSearch kế thừa từ lớp Driver chứa các test case
class TestNavigation(Driver):

    def test_navigation_gundam_link(self, driver):
        # Navigate to the home page
        driver.get("http://localhost:8000/")
        navigation = Navigation(driver)
        navigation.click_gundam()
        header = navigation.get_text_h1()
        assert header == "Gundam", f"Expected name not found. Got {header}"

    def test_navigation_gundam_hover_link(self, driver):
        # Navigate to the home page
        driver.get("http://localhost:8000/")
        navigation = Navigation(driver)
        navigation.hover_and_click_gundam_PG()
        header = navigation.get_text_h1()
        assert header == "Gundam PG", f"Expected name not found. Got {header}"

    def test_product_details(self, driver):
        driver.get("http://localhost:8000/")
        navigation = Navigation(driver)
        navigation.click_gundam()
        navigation.click_random_product(True)
        name = navigation.get_product_name()
        assert [name] == navigation.get_added_products(), f"Expected name not found. Got {name}"

    def test_navigation_link_category_gundam(self, driver):
        driver.get("http://localhost:8000/")
        navigation = Navigation(driver)
        xpath_list = [
            "/html/body/div[2]/div/div/div[1]/div/a",  # Link Gundam
            "/html/body/div[2]/div/div/div[2]/div/a",
            "/html/body/div[2]/div/div/div[4]/div/a",
            "/html/body/div[2]/div/div/div[3]/div/a"
        ]
        expected_headers = ["Gundam RG", "Gundam MG", "Gundam PG", "Gundam HG"]
        navigation.test_navigation_links(driver, xpath_list, expected_headers)

    def test_data_navigation_category_hg(self, driver):
        driver.get("http://localhost:8000/")
        navigation = Navigation(driver)
        navigation.click_menu_hg()
        data = TestData.load_data('product_data.json')['HG']
        product_names = navigation.data_validation_show_product()
        assert product_names == data

    def test_data_navigation_category_pg(self, driver):
        driver.get("http://localhost:8000/")
        navigation = Navigation(driver)
        navigation.hover_and_click_gundam_PG()
        data = TestData.load_data('product_data.json')['PG']
        product_names = navigation.data_validation_show_product()
        assert product_names == data

    def test_data_navigation_category_mg(self, driver):
        driver.get("http://localhost:8000/")
        navigation = Navigation(driver)
        navigation.click_menu_mg()
        data = TestData.load_data('product_data.json')['MG']
        product_names = navigation.data_validation_show_product()
        assert product_names == data

    def test_data_navigation_category_rg(self, driver):
        driver.get("http://localhost:8000/")
        navigation = Navigation(driver)
        navigation.click_menu_rg()
        data = TestData.load_data('product_data.json')['RG']
        product_names = navigation.data_validation_show_product()
        assert product_names == data




