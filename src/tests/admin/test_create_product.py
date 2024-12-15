import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import function
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def test_create_successful(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_product(driver)
    function.add_image_product(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")
    function.create_product(driver, "Pikachu", "250000", "0", "Pokemon hệ điện", "10")
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    function.navigate_to_list_product(driver)
    product = driver.find_elements(By.XPATH, "//th[contains(text(), 'Pikachu')]")
    assert "Thêm mới thành công" in message and len(product) != 0

def test_create_with_empty_productname(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_product(driver)
    function.add_image_product(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")
    function.create_product(driver, "", "250000", "0", "Pokemon hệ điện", "10")
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Tên sản phẩm không được để trống" in message

def test_create_with_invalid_price(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_product(driver)
    function.add_image_product(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")
    function.create_product(driver, "Pikachu1", "-250000", "0", "Pokemon hệ điện", "10")
    function.navigate_to_list_product(driver)
    product = driver.find_elements(By.XPATH, "//th[contains(text(), 'Pikachu1')]")
    assert len(product) == 0
    
def test_create_with_invalid_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_product(driver)
    function.add_image_product(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\function.py")
    function.create_product(driver, "Pikachu2", "250000", "0", "Pokemon hệ điện", "10")
    function.navigate_to_list_product(driver)
    product = driver.find_elements(By.XPATH, "//th[contains(text(), 'Pikachu2')]")
    assert len(product) == 0

def test_create_with_empty_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_product(driver)
    function.create_product(driver, "Pikachu", "250000", "0", "Pokemon hệ điện", "10", )
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Ảnh sản phẩm không được để trống" in message
    