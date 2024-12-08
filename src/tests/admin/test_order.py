import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from login_helper import login
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

@pytest.fixture
def driver():
    driver = webdriver.Edge()  # Thay đổi nếu dùng trình duyệt khác
    yield driver
    driver.quit()


def test_check_order_displayed(driver):
    # Login to the system
    login(driver)
    
    # Navigate to the order list page
    order_link = driver.find_element(By.XPATH, "//a[@class='nav-link' and contains(., 'Order')]")
    order_link.click()
    driver.find_element(By.XPATH, "/html/body/div/aside/div/nav[4]/ul/li/ul/li/a").click()
    time.sleep(3)  # Wait for the page to load
    
    # Kiểm tra các cột có hiển thị đầy đủ không
    try:
        columns = ["ID","Name","Email","Phone", "Address", "Total", "Date Created", "Status"]
        for column in columns:
            header = driver.find_element(By.XPATH, f"//th[contains(text(), '{column}')]")
            assert header.is_displayed(), f"Cột {column} không được hiển thị."
    except NoSuchElementException as e:
        pytest.fail(f"Không tìm thấy cột: {e}")

    # Kiểm tra trạng thái đơn hàng hiển thị đúng màu sắc và thông tin
    statuses = {
        "completed": "badge bg-success",
        "pending": "badge bg-warning",
        "canceled": "badge bg-danger"
    }

    # Lấy danh sách tất cả các trạng thái trong bảng
    order_rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    assert len(order_rows) > 0, "Không có đơn hàng nào trong danh sách."

    for row in order_rows:
        status_element = row.find_element(By.XPATH, ".//span[contains(@class, 'badge')]")
        status_text = status_element.text.strip().lower()
        class_attr = status_element.get_dom_attribute("class")

        if status_text in statuses:
            expected_class = statuses[status_text]
            assert expected_class in class_attr, f"Trạng thái '{status_text}' không có màu sắc đúng."

    # Kiểm tra số lượng đơn hàng hiển thị
    displayed_order_count = len(order_rows)
    # Giả sử hệ thống có tổng số đơn hàng hiển thị trên giao diện (ví dụ: 10 đơn)
    assert displayed_order_count > 0, "Danh sách đơn hàng không có dữ liệu."

def test_view_order_details(driver):
    login(driver)
    
    # Navigate to the order list page
    order_link = driver.find_element(By.XPATH, "//a[@class='nav-link' and contains(., 'Order')]")
    order_link.click()
    driver.find_element(By.XPATH, "/html/body/div/aside/div/nav[4]/ul/li/ul/li/a").click()
    time.sleep(3)  # Wait for the page to load

    # Lấy thông tin đơn hàng đầu tiên trong danh sách
    first_order = driver.find_element(By.XPATH, "//table/tbody/tr[1]")
    
    # Lấy thông tin từ hàng đầu tiên
    phone_list_page = first_order.find_element(By.XPATH, ".//th[4]").text.strip()
    email_list_page = first_order.find_element(By.XPATH, ".//th[3]").text.strip()
    name_list_page = first_order.find_element(By.XPATH, ".//th[2]").text.strip()
    # total_list_page = first_order.find_element(By.XPATH,".//th[6]").text.strip()
    
    # Click vào biểu tượng chỉnh sửa (icon bút xanh)
    edit_button = first_order.find_element(By.XPATH, ".//a[@class='btn btn-primary']")  # Điều chỉnh class nếu cần
    edit_button.click()

    # Lấy thông tin từ trang chi tiết
    phone_label = driver.find_element(By.XPATH, "//div[@class='col-sm-4 invoice-col'][contains(., 'Phone:')]")
    phone_text = phone_label.text  # Lấy toàn bộ nội dung văn bản
    email_label = driver.find_element(By.XPATH, "//div[@class='col-sm-4 invoice-col'][contains(., 'Email:')]")
    email_text = email_label.text  # Lấy toàn bộ nội dung văn bản
    name_text = driver.find_element(By.XPATH, "//div[@class='col-sm-4 invoice-col']/address/strong")
    name_detail_page = name_text.text
    
    match_phone = re.search(r"Phone:\s*([^\n]+)", phone_text)  # Tìm nội dung sau "Phone:" đến khi xuống dòng
    phone_detail_page = match_phone.group(1).strip()  # Lấy nhóm đầu tiên (nội dung sau "Phone:")
    match_email = re.search(r"Email:\s*([^\n]+)", email_text)  # Tìm nội dung sau "Phone:" đến khi xuống dòng
    email_detail_page = match_email.group(1).strip()  
   
    
    # Bước 3: So sánh thông tin giữa trang danh sách và trang chi tiết
    assert phone_list_page == phone_detail_page, f"Số điện thoại không khớp: {phone_list_page} != {phone_detail_page}"
    assert email_list_page == email_detail_page, f"Địa chỉ không khớp: {email_list_page} != {email_detail_page}"
    assert name_list_page == name_detail_page, f"Tổng tiền không khớp: {name_list_page} != {name_detail_page}"
    

def test_update_order_status(driver):
    login(driver)
    
    # Navigate to the order list page
    order_link = driver.find_element(By.XPATH, "//a[@class='nav-link' and contains(., 'Order')]")
    order_link.click()
    driver.find_element(By.XPATH, "/html/body/div/aside/div/nav[4]/ul/li/ul/li/a").click()
    time.sleep(3)  # Wait for the page to load
    first_order_old = driver.find_element(By.XPATH, "//table/tbody/tr[1]")
    edit_button = first_order_old.find_element(By.XPATH, ".//a[@class='btn btn-primary']")  # Điều chỉnh class nếu cần
    edit_button.click()
    time.sleep(3)
    status = driver.find_element(By.XPATH,"//div[@class='col-6']/p/span")
    status_text= status.text
    if status_text != "completed" and status_text != "canceled" :
        ship_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success.float-right")
        ship_button.click()
        time.sleep(5)
        status = driver.find_element(By.XPATH,"//div[@class='col-6']/p/span")
        status_text= status.text  
    driver.get('http://127.0.0.1:8000/admin/orders/list')
    time.sleep(3)
    first_order_new = driver.find_element(By.XPATH, "//table/tbody/tr[1]")
    status_list_page = first_order_new.find_element(By.XPATH, ".//th[8]/span").text

    assert status_text == status_list_page,f"Status khong dung:{status_text} != {status_list_page}"





