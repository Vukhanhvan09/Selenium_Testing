# BÁO CÁO THỰC HÀNH KIỂM THỬ TỰ ĐỘNG VỚI SELENIUM

## 1. Mục tiêu bài thực hành

- Tìm hiểu công cụ **Selenium WebDriver** qua tài liệu hướng dẫn.
- Sử dụng **Python**, **Selenium** và **Pytest** để tự động hóa thao tác trên website.
- Xây dựng và thực hiện **tối thiểu 05 test case**.
- Đánh giá kết quả thực thi dựa trên các điều kiện kiểm tra (`assert`).

## 2. Giới thiệu công cụ Selenium

**Selenium** là bộ công cụ mã nguồn mở hỗ trợ tự động hóa trình duyệt web. **Selenium WebDriver** cho phép chương trình điều khiển trình duyệt, thực hiện các thao tác như nhập dữ liệu, nhấn nút, chọn danh sách và đọc nội dung trên trang.

Trong bài thực hành, Selenium WebDriver được sử dụng kết hợp với:

| Thành phần | Vai trò |
|---|---|
| Python | Ngôn ngữ lập trình các kịch bản kiểm thử |
| Selenium WebDriver | Tự động điều khiển trình duyệt Chrome |
| Pytest | Tổ chức test case, chạy kiểm thử và báo cáo PASS/FAIL |
| Google Chrome | Trình duyệt thực thi kiểm thử |
| SauceDemo | Website mẫu dùng để kiểm thử |

**Tài liệu tham khảo:**

- [Selenium WebDriver Documentation](https://www.selenium.dev/documentation/webdriver/)
- [Selenium – First Steps](https://www.selenium.dev/documentation/webdriver/getting_started/)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)

## 3. Website và phạm vi kiểm thử

- **Website:** [https://www.saucedemo.com/](https://www.saucedemo.com/)
- **Loại website:** Website mô phỏng bán hàng trực tuyến.
- **Tài khoản thử nghiệm:** `standard_user`
- **Mật khẩu thử nghiệm:** `secret_sauce`

**Phạm vi:** Kiểm thử đăng nhập thành công, đăng nhập không thành công, sắp xếp sản phẩm, thêm sản phẩm vào giỏ hàng và đăng xuất. SauceDemo có chức năng **sắp xếp** sản phẩm, vì vậy bài thực hành sử dụng chức năng này thay cho tìm kiếm.

## 4. Thiết kế test case

| Mã test case | Chức năng | Dữ liệu/bước thực hiện chính | Kết quả mong đợi |
|---|---|---|---|
| TC01 | Đăng nhập thành công | Nhập `standard_user` / `secret_sauce`, chọn **Login** | Chuyển đến trang `/inventory.html` |
| TC02 | Đăng nhập sai mật khẩu | Nhập `standard_user` / `wrong_password`, chọn **Login** | Hiển thị thông báo tài khoản hoặc mật khẩu không khớp |
| TC03 | Sắp xếp giá tăng dần | Đăng nhập, chọn **Price (low to high)** | Giá sản phẩm được hiển thị theo thứ tự không giảm |
| TC04 | Thêm sản phẩm vào giỏ hàng | Đăng nhập, thêm **Sauce Labs Backpack**, mở giỏ hàng | Trong giỏ hàng có **Sauce Labs Backpack** |
| TC05 | Đăng xuất | Đăng nhập, mở menu, chọn **Logout** | Quay về trang đăng nhập và hiển thị nút **Login** |

### 4.1. TC01 – Đăng nhập thành công

1. Mở `https://www.saucedemo.com/`.
2. Nhập tên đăng nhập `standard_user`.
3. Nhập mật khẩu `secret_sauce`.
4. Nhấn **Login**.
5. Kiểm tra URL hiện tại chứa `/inventory.html`.

**Kết quả mong đợi:** Người dùng truy cập thành công trang danh sách sản phẩm.

### 4.2. TC02 – Đăng nhập sai mật khẩu

1. Mở trang đăng nhập.
2. Nhập tên đăng nhập `standard_user`.
3. Nhập mật khẩu sai `wrong_password`.
4. Nhấn **Login**.
5. Kiểm tra thông báo lỗi được hiển thị.

**Kết quả mong đợi:** Trang hiển thị thông báo có nội dung `Username and password do not match`.

### 4.3. TC03 – Sắp xếp sản phẩm theo giá tăng dần

1. Đăng nhập bằng tài khoản hợp lệ.
2. Trong danh sách sắp xếp, chọn **Price (low to high)**.
3. Lấy giá của tất cả sản phẩm đang hiển thị.
4. So sánh danh sách giá thực tế với danh sách giá được sắp xếp tăng dần.

**Kết quả mong đợi:** Danh sách giá thực tế bằng danh sách đã sắp xếp tăng dần.

### 4.4. TC04 – Thêm sản phẩm vào giỏ hàng

1. Đăng nhập bằng tài khoản hợp lệ.
2. Nhấn **Add to cart** của sản phẩm **Sauce Labs Backpack**.
3. Mở trang giỏ hàng.
4. Kiểm tra tên sản phẩm xuất hiện trong giỏ hàng.

**Kết quả mong đợi:** Giỏ hàng chứa sản phẩm **Sauce Labs Backpack**.

### 4.5. TC05 – Đăng xuất

1. Đăng nhập bằng tài khoản hợp lệ.
2. Nhấn biểu tượng menu.
3. Chờ mục **Logout** có thể được nhấn.
4. Nhấn **Logout**.
5. Kiểm tra URL quay về trang chủ và nút **Login** xuất hiện.

**Kết quả mong đợi:** Phiên đăng nhập kết thúc; giao diện đăng nhập được hiển thị.

## 5. Chuẩn bị môi trường và cài đặt

**Yêu cầu:** Python 3, Google Chrome và kết nối Internet để truy cập website thử nghiệm.

Cài đặt thư viện:

```bash
python -m pip install selenium pytest
```

Có thể tạo file `requirements.txt` với nội dung:

```text
selenium
pytest
```

Sau đó cài đặt bằng lệnh:

```bash
python -m pip install -r requirements.txt
```

Selenium phiên bản mới có **Selenium Manager**, thường tự hỗ trợ tìm và quản lý driver phù hợp. Nếu cấu hình máy có hạn chế truy cập mạng hoặc trình duyệt đặc biệt, có thể cần cấu hình driver riêng.

**Cấu trúc thư mục đề xuất:**

```text
Selenium_Testing/
├── README.md
├── requirements.txt
└── test_saucedemo.py
```

## 6. Mã nguồn kiểm thử tự động

Tạo file `test_saucedemo.py` với nội dung sau:

```python
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
```

### Giải thích một số câu lệnh chính

| Lệnh | Ý nghĩa |
|---|---|
| `webdriver.Chrome()` | Khởi tạo trình duyệt Chrome để kiểm thử |
| `find_element(By.ID, ...)` | Tìm một phần tử theo thuộc tính `id` |
| `send_keys(...)` | Nhập dữ liệu vào ô nhập liệu |
| `click()` | Thực hiện thao tác nhấn |
| `Select(...).select_by_value(...)` | Chọn một tùy chọn trong danh sách thả xuống |
| `WebDriverWait(...).until(...)` | Chờ cho đến khi điều kiện được đáp ứng |
| `assert` | So sánh kết quả thực tế với kết quả mong đợi |
| `@pytest.fixture` | Chuẩn bị và dọn dẹp tài nguyên cho mỗi test case |

## 7. Hướng dẫn chạy kiểm thử

Tại thư mục chứa file `test_saucedemo.py`, mở Terminal và chạy:

```bash
python -m pytest test_saucedemo.py -v
```

Muốn lưu kết quả để đưa vào báo cáo, chạy:

```bash
python -m pytest test_saucedemo.py -v > ket_qua_kiem_thu.txt
```

Khi chạy, Pytest sẽ gọi các hàm có tên bắt đầu bằng `test_`. Mỗi test case sử dụng một phiên Chrome mới; sau mỗi bài kiểm thử, trình duyệt được đóng bằng `browser.quit()`.

**Ví dụ kết quả khi tất cả test case thành công (minh họa, chưa phải kết quả thực tế):**

```text
test_saucedemo.py::test_login_success PASSED
test_saucedemo.py::test_login_invalid_password PASSED
test_saucedemo.py::test_sort_price_ascending PASSED
test_saucedemo.py::test_add_to_cart PASSED
test_saucedemo.py::test_logout PASSED

======================= 5 passed =======================
```

## 8. Kết quả thực nghiệm

> **Lưu ý:** Chưa thực thi kiểm thử trong môi trường của sinh viên. Các ô bên dưới cần được cập nhật sau khi chạy chương trình, không được mặc định ghi PASS khi chưa có bằng chứng.

| Mã test case | Kết quả mong đợi | Kết quả thực tế | Trạng thái |
|---|---|---|---|
| TC01 | Truy cập được trang sản phẩm | Chưa ghi nhận | Chưa chạy |
| TC02 | Hiển thị thông báo lỗi đăng nhập | Chưa ghi nhận | Chưa chạy |
| TC03 | Sản phẩm được sắp xếp đúng theo giá tăng dần | Chưa ghi nhận | Chưa chạy |
| TC04 | Sản phẩm xuất hiện trong giỏ hàng | Chưa ghi nhận | Chưa chạy |
| TC05 | Quay về trang đăng nhập | Chưa ghi nhận | Chưa chạy |

**Minh chứng cần bổ sung:**

- Ảnh màn hình Terminal hiển thị kết quả chạy 5 test case.
- Ảnh quá trình đăng nhập thành công và thông báo lỗi đăng nhập.
- Ảnh trang sản phẩm sau khi sắp xếp theo giá.
- Ảnh sản phẩm trong giỏ hàng.
- Ảnh trang đăng nhập sau khi đăng xuất.

Nếu test case thất bại, cần ghi rõ thông báo lỗi, tình huống xảy ra và hướng xử lý; không chỉnh sửa kết quả kiểm thử để phù hợp với kỳ vọng.

## 9. Nhận xét và kết luận

Bài thực hành xây dựng 5 kịch bản kiểm thử tự động cho các luồng chức năng cơ bản của website SauceDemo. Qua việc xây dựng chương trình, sinh viên có thể làm quen với việc định vị phần tử trên trang web, mô phỏng thao tác người dùng và xác minh kết quả bằng câu lệnh `assert`.

Selenium giúp giảm thao tác lặp lại so với kiểm thử thủ công, đồng thời có thể tái chạy các kịch bản sau khi hệ thống thay đổi. Tuy nhiên, kết quả kiểm thử vẫn phụ thuộc vào tính ổn định của website, trình duyệt, kết nối mạng và cách chọn bộ định vị phần tử. Trong quá trình phát triển thực tế, nên tăng cường cơ chế chờ điều kiện, bổ sung dữ liệu kiểm thử và kiểm thử các trường hợp biên.

**Kết luận cuối cùng về tỷ lệ PASS/FAIL chỉ được đưa ra sau khi chạy bộ kiểm thử và ghi nhận kết quả thực tế.**
