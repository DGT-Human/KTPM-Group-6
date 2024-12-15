import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver, email, password):
    driver.get("http://127.0.0.1:8000/")
    driver.find_element(By.XPATH, "/html/body/header/div[1]/div/nav/div[2]/div[3]").click()
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/aside/div[2]/div[2]/ul/li[3]/a").click()    
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[1]/input").send_keys(email)
    driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[2]/input").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[4]/button").click()    
    time.sleep(1) 
    
def navigate_to_create_product(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[2]/ul/li/a/i").click()    
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[2]/ul/li/ul/li[1]/a/i").click()    
    time.sleep(1) 

def navigate_to_list_product(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[2]/ul/li/a/i").click()    
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[2]/ul/li/ul/li[2]/a/i").click()    
    time.sleep(1) 

def navigate_to_create_category(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[1]/ul/li/a/i").click()    
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[1]/ul/li/ul/li[1]/a/i").click()    
    time.sleep(1) 
    
def navigate_to_list_category(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[1]/ul/li/a/i").click()    
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[1]/ul/li/ul/li[2]/a/i").click()    
    time.sleep(1)
    
def navigate_to_create_slider(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[3]/ul/li/a/i").click()    
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[3]/ul/li/ul/li[1]/a/i").click()    
    time.sleep(1) 
    
def navigate_to_list_slider(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[3]/ul/li/a/i").click()    
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/nav[3]/ul/li/ul/li[2]/a/i").click()    
    time.sleep(1)
    
def create_product(driver, name, price, sale, describe, quan):
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[1]/div/input").send_keys(name)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/select").click()    
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/select/option[8]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/div[1]/div/input").send_keys(price)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/input").send_keys(sale)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/textarea").send_keys(describe)   
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[4]/input").send_keys(quan)   
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame'))
    content_editable = driver.find_element(By.TAG_NAME, 'p')
    content_editable.send_keys(describe)
    driver.switch_to.default_content()
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    
def add_image_product(driver, image):
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[6]/input[1]").send_keys(image)   
    time.sleep(3)  
    
def create_category(driver, name, describe):
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/input").send_keys(name)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select").click()
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[2]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/textarea").send_keys(describe)
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame'))
    driver.find_element(By.TAG_NAME, 'p').send_keys(describe)
    driver.switch_to.default_content()
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    
def add_image_category(driver, image):
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[5]/input[1]").send_keys(image)   
    time.sleep(3)   

def create_slider(driver, name, url):
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[1]/div/input").send_keys(name)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/input").send_keys(url)
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[2]/button")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    
def add_image_slider(driver, image):
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/form/div[1]/div[3]/input[1]").send_keys(image)   
    time.sleep(3) 