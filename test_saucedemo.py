
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

def login(driver, username="standard_user", password="secret_sauce"):
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

# TC01: Đăng nhập thành công
def test_login_success(driver):
    login(driver)
    assert "/inventory.html" in driver.current_url

# TC02: Đăng nhập sai mật khẩu
def test_login_invalid_password(driver):
    login(driver, password="wrong_password")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Username and password do not match" in error.text

# TC03: Sắp xếp sản phẩm theo giá tăng dần
def test_sort_price_ascending(driver):
    login(driver)
    sort = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort.select_by_value("lohi")

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_values = [float(p.text.replace("$", "")) for p in prices]

    assert price_values == sorted(price_values)

# TC04: Thêm sản phẩm vào giỏ hàng
def test_add_to_cart(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert item.text == "Sauce Labs Backpack"

# TC05: Đăng xuất
def test_logout(driver):
    login(driver)
    driver.find_element(By.ID, "react-burger-menu-btn").click()

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_button.click()

    assert driver.current_url.rstrip("/") == URL.rstrip("/")
    assert driver.find_element(By.ID, "login-button").is_displayed()
