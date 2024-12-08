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
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[1]/div/input").send_keys("abc")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/input").send_keys("https://fontawesome.com/search?q=image&o=r")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/input[1]").send_keys(r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")   
    time.sleep(3) 
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "thành công" in message
    
def test_create_with_empty_slider_name(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_slider(driver)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/input").send_keys("https://fontawesome.com/search?q=image&o=r")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/input[1]").send_keys(r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")   
    time.sleep(3) 
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Tên không được để trống" in message
    
def test_create_with_empty_url(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_slider(driver)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[1]/div/input").send_keys("abc")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/input[1]").send_keys(r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")   
    time.sleep(3) 
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Url không được để trống" in message
    
def test_create_with_empty_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_slider(driver)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[1]/div/input").send_keys("abc")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/input").send_keys("https://fontawesome.com/search?q=image&o=r")
    time.sleep(3) 
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Ảnh không được để trống" in message
    
def test_create_with_invalid_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_slider(driver)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[1]/div/input").send_keys("abc")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/input").send_keys("https://fontawesome.com/search?q=image&o=r")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/input[1]").send_keys(r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\function.py")   
    time.sleep(3) 
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "thành công" not in message