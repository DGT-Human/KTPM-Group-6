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
    function.navigate_to_create_slider(driver)
    function.add_image_slider(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")
    function.create_slider(driver, "abc", "https://fontawesome.com/search?q=image&o=r")
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    function.navigate_to_list_slider(driver)
    slider = driver.find_elements(By.XPATH, "//th[contains(text(), 'abc')]")
    assert "Thêm Slider thành công" in message and len(slider) != 0
    
def test_create_with_empty_slider_name(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_slider(driver)
    function.add_image_slider(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")
    function.create_slider(driver, "", "https://fontawesome.com/search?q=image&o=r")
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Tên không được để trống" in message
    
def test_create_with_empty_url(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_slider(driver)
    function.add_image_slider(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")
    function.create_slider(driver, "abc", "")
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Url không được để trống" in message
    
def test_create_with_empty_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_slider(driver)
    function.create_slider(driver, "abc", "https://fontawesome.com/search?q=image&o=r")
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Ảnh không được để trống" in message
    
def test_create_with_invalid_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_slider(driver)
    function.add_image_slider(driver, r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\function.py")
    function.create_slider(driver, "xyz", "https://fontawesome.com/search?q=image&o=r")
    function.navigate_to_list_slider(driver)
    slider = driver.find_elements(By.XPATH, "//th[contains(text(), 'xyz')]")
    assert len(slider) == 0