import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.added_products = []

    def scroll_to(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y});")

    def scroll_to_element(self, element):
        """Cuộn đến một phần tử cụ thể trên trang."""
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        time.sleep(1)

    def get(self, url):
        self.driver.get(url)