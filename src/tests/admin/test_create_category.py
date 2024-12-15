import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    function.navigate_to_create_category(driver)
    function.add_image_category(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")
    function.create_category(driver, "Bakugan", "abc")
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    function.navigate_to_list_category(driver)
    category = driver.find_elements(By.XPATH, "//th[contains(text(), 'Bakugan')]")
    assert "Dữ liệu đã được thêm thành công" in message and len(category) != 0
    
def test_create_with_empty_category_name(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_category(driver)
    function.add_image_category(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")
    function.create_category(driver, "", "abc")
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "The name field is required." in message

def test_create_with_invalid_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_category(driver)
    function.add_image_category(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\function.py")
    function.create_category(driver, "Bakugan1", "abc")
    function.navigate_to_list_category(driver)
    category = driver.find_elements(By.XPATH, "//th[contains(text(), 'Bakugan1')]")
    assert len(category) == 0 
    
def test_create_with_empty_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_category(driver)
    function.create_category(driver, "Bakugan2", "abc")
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    function.navigate_to_list_category(driver)
    category = driver.find_elements(By.XPATH, "//th[contains(text(), 'Bakugan2')]")
    assert "thành công" in message and len(category) != 0
    
def test_create_with_duplicate_category_name(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_category(driver)
    function.add_image_category(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")
    function.create_category(driver, "POKEMON", "abc")
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Thêm menu thất bại" in message
