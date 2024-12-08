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