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
    
def test_delete_successful(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_list_slider(driver)    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/table/tbody/tr[1]/th[7]/a[2]/i").click()    
    time.sleep(1)
    driver.switch_to.alert.accept()  
    time.sleep(5)
    message = driver.switch_to.alert.text
    assert "Xóa thành công" in message
    
def test_delete_when_session_expires(driver):
    function.login(driver, "admin@localhost.com", "02062003")  
    function.navigate_to_list_slider(driver)    
    driver.delete_all_cookies()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/table/tbody/tr[1]/th[7]/a[2]/i").click()    
    time.sleep(1)
    driver.switch_to.alert.accept()  
    time.sleep(5)
    assert "list#" in driver.current_url