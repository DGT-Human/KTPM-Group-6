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
    
def test_update_successful(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_list_slider(driver)    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/table/tbody/tr[1]/th[7]/a[1]/i").click()    
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[1]/div/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[1]/div/input").send_keys("xyz")
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "thành công" in message
    
def test_update_with_empty_slider_name(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_list_slider(driver)    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/table/tbody/tr[1]/th[7]/a[1]/i").click()    
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[1]/div/input").clear()
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Tên không được để trống" in message
    
def test_update_with_empty_url(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_list_slider(driver)    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/table/tbody/tr[1]/th[7]/a[1]/i").click()    
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/input").clear()
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "Url không được để trống" in message
    
def test_update_with_invalid_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_list_slider(driver)    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/table/tbody/tr[1]/th[7]/a[1]/i").click()    
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/input[1]").send_keys(r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\function.py")
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "thành công" not in message