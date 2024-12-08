import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.tests.admin.login_helper import login
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

@pytest.fixture
def driver():
    driver = webdriver.Edge()  # Thay đổi nếu dùng trình duyệt khác
    yield driver
    driver.quit()


def test_account_displayed_column(driver):
    # Step 1: Login to the system
    login(driver)
    
    # Step 2: Navigate to the order list page
    order_link = driver.find_element(By.XPATH, "//a[@class='nav-link' and contains(., 'Customer')]")
    order_link.click()
    driver.find_element(By.XPATH, "/html/body/div/aside/div/nav[5]/ul/li/ul/li/a").click()
    time.sleep(3)  # Wait for the page to load
    #Kiểm tra rằng bảng danh sách hiển thị đầy đủ các cột
    columns = ["ID", "Name", "Email", "Phone", "Address", "Date Created"]
    table_headers = driver.find_elements(By.XPATH, "//table//th")  # Lấy tất cả tiêu đề cột

    for i, column in enumerate(columns):
        assert table_headers[i].text == column, f"Cột {column} không hiển thị đúng."


def change_account_infor(driver, account_data):
    login(driver)
    
    # Step 2: Navigate to the order list page
    order_link = driver.find_element(By.XPATH, "//a[@class='nav-link' and contains(., 'Customer')]")
    order_link.click()
    driver.find_element(By.XPATH, "/html/body/div/aside/div/nav[5]/ul/li/ul/li/a").click()
    time.sleep(3)  #
    # Tìm hàng đầu tiên trong bảng tài khoản
    first_account_row = driver.find_element(By.XPATH, "//table//tbody//tr[1]")

    # Lưu thông tin ban đầu từ danh sách tài khoản
    initial_name = first_account_row.find_element(By.XPATH, "./th[2]").text
    initial_phone = first_account_row.find_element(By.XPATH, "./th[4]").text
    initial_adress = first_account_row.find_element(By.XPATH, "./th[5]").text

    # Click vào biểu tượng chỉnh sửa (icon bút xanh)
    edit_button = first_account_row.find_element(By.XPATH, ".//a[@class='btn btn-primary']")
    edit_button.click()

    # Chỉnh sửa thông tin
    name_field = driver.find_element(By.NAME, "name")  # Tên trường có thể thay đổi
    name_field.clear()
    name_field.send_keys(account_data["name"])

    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.clear()
    phone_field.send_keys(account_data["phone"])

    address_field = driver.find_element(By.NAME, "address")
    address_field.clear()
    address_field.send_keys(account_data["address"])

    # Click nút "Submit"
    submit_button = driver.find_element(By.XPATH, "//div[@class='card-footer']/button[@class='btn btn-primary']")
    submit_button.click()

    # Quay lại danh sách tài khoản và kiểm tra thông tin cập nhật
    driver.get("http://127.0.0.1:8000/admin/accounts/list")

    # Tìm hàng đầu tiên và xác nhận thông tin đã được cập nhật
    updated_name = driver.find_element(By.XPATH, "//table//tbody//tr[1]/th[2]").text
    updated_phone = driver.find_element(By.XPATH, "//table//tbody//tr[1]/th[4]").text
    updated_adress = driver.find_element(By.XPATH, "//table//tbody//tr[1]/th[5]").text

    # So sánh kết quả
    assert updated_name != initial_name, "Name không được cập nhật chính xác"
    assert updated_phone != initial_phone, "Phone không được cập nhật chính xác"
    assert updated_adress != initial_adress, "Phone không được cập nhật chính xác"
    
def test_change_account_infor(driver):
    account_data = {
        "name": "Nhan",
        "phone": "123456789",
        "address": "TPHCM"
    }
    password_data={
        "password":"123456",
        
    }
    change_account_infor(driver, account_data)
    test_change_password_user(driver,password_data)

def test_submit_with_empty_data(driver):
    login(driver)
    
    # Navigate to the customer list page
    order_link = driver.find_element(By.XPATH, "//a[@class='nav-link' and contains(., 'Customer')]")
    order_link.click()
    
    # Click on the link to open the account details page
    customer_detail_link = driver.find_element(By.XPATH, "/html/body/div/aside/div/nav[5]/ul/li/ul/li/a")
    customer_detail_link.click()
    first_account_row = driver.find_element(By.XPATH, "//table//tbody//tr[1]")
    edit_button = first_account_row.find_element(By.XPATH, ".//a[@class='btn btn-primary']")
    edit_button.click()
    name_field = driver.find_element(By.NAME, "name")  # Tên trường có thể thay đổi
    name_field.clear()
    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.clear()
    address_field = driver.find_element(By.NAME, "address")
    address_field.clear()
    # Click the 'Submit' button
    submit_button = driver.find_element(By.XPATH, "//div[@class='card-footer']/button[@class='btn btn-primary']")  # Adjust based on actual element
    submit_button.click()
    time.sleep(3)

def test_change_password_user(driver,password_data):
    login(driver)
    
    # Navigate to the order list page
    order_link = driver.find_element(By.XPATH, "//a[@class='nav-link' and contains(., 'Customer')]")
    order_link.click()
    driver.find_element(By.XPATH, "/html/body/div/aside/div/nav[5]/ul/li/ul/li/a").click()
    time.sleep(3)  #

    first_account_row = driver.find_element(By.XPATH, "//table//tbody//tr[1]")
    edit_button = first_account_row.find_element(By.XPATH, ".//a[@class='btn btn-primary']")
    edit_button.click()

    reset_button = driver.find_element(By.XPATH, "//div[@class='card-footer']/button[@class='btn btn-danger']")
    reset_button.click()
    time.sleep(3)
    new_password = driver.find_element(By.ID,'newPassword')
    new_password.send_keys(password_data["password"])
    new_password = driver.find_element(By.ID,'confirmPassword')
    new_password.send_keys(password_data["password"])
    time.sleep(3)
    submit_button = driver.find_element(By.XPATH, "//div[@class='modal-footer']/button[@class='btn btn-primary']")
    submit_button.click()
    time.sleep(3)
    alert = driver.find_element(By.XPATH,"//div[@class='alert alert-success']")
    alert_text = alert.text

    assert alert_text


def test_responsive_design(driver):
    # Kiểm tra ở kích thước màn hình di động
    driver.get('http://127.0.0.1:8000')
    driver.set_window_size(375, 667)  # Kích thước màn hình di động
      # Thay đổi URL nếu cần
    time.sleep(2)  # Đợi trang tải

    # Kiểm tra xem menu có hiển thị đúng không
    logo = driver.find_element(By.XPATH, "//div[@class='logo-mobile']/a/img")
    assert logo.is_displayed(), "Logo không hiển thị ở chế độ di động."

    # Kiểm tra xem các nút có hiển thị đúng không
    menu = driver.find_element(By.XPATH, "//span[@class='hamburger-box']")
    assert menu.is_displayed(), "Menu không hiển thị ở chế độ di động."

    # Kiểm tra ở kích thước màn hình máy tính
    driver.set_window_size(1024, 768)  # Kích thước màn hình máy tính
      # Thay đổi URL nếu cần
    time.sleep(2)  # Đợi trang tải
    menu = driver.find_element(By.XPATH, "//a[@class='logo']/img")
    logo = driver.find_element(By.XPATH, "//i[@class='zmdi zmdi-menu']")
    
    assert menu.is_displayed(), "Menu không hiển thị ở chế độ máy tính."
    assert logo.is_displayed(), "Logo không hiển thị ở chế độ máy tính."

