# login_helper.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()  # Thay đổi nếu dùng trình duyệt khác
    yield driver
    driver.quit()

def login(driver):
        driver.get("http://127.0.0.1:8000/users/login")
        
        
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        
        email_input.clear()
        email_input.send_keys("admin@localhost.com")
        
        password_input.clear()
        password_input.send_keys("02062003")
        
        login_button = driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[4]/button")
        login_button.click()
        
