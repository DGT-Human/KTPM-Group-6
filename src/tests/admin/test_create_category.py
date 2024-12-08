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
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/input").send_keys("Bakugan")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select").click()
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/textarea").send_keys("Bakugan")
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame'))
    driver.find_element(By.TAG_NAME, 'p').send_keys("Bakugan")
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[5]/input[1]").send_keys(r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")   
    time.sleep(3)  
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "thành công" in message
    
def test_create_with_empty_category_name(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_category(driver)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select").click()
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/textarea").send_keys("Bakugan")
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame'))
    driver.find_element(By.TAG_NAME, 'p').send_keys("Bakugan")
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[5]/input[1]").send_keys(r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\pikachu.jpg")   
    time.sleep(3)  
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "The name field is required." in message

def test_create_with_invalid_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_category(driver)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/input").send_keys("Bakugan")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select").click()
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/textarea").send_keys("Bakugan")
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame'))
    driver.find_element(By.TAG_NAME, 'p').send_keys("Bakugan")
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[5]/input[1]").send_keys(r"C:\Users\maiha\OneDrive\Documents\Visual Studio 2017\Software testing\test_xampp\a.cpp")   
    time.sleep(3)  
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "thành công" not in message
    
def test_create_with_empty_image(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_category(driver)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/input").send_keys("Bakugan")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select").click()
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/textarea").send_keys("Bakugan")
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame'))
    driver.find_element(By.TAG_NAME, 'p').send_keys("Bakugan")
    driver.switch_to.default_content()
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "thành công" in message
    
def test_create_with_duplicate_category_name(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_create_category(driver)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/input").send_keys("TOOLS")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select").click()
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/textarea").send_keys("Bakugan")
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame'))
    driver.find_element(By.TAG_NAME, 'p').send_keys("Bakugan")
    driver.switch_to.default_content()
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    message = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[1]/div/div[1]").text
    assert "thất bại" in message
