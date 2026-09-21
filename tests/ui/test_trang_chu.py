from pages.home_page import HomePage

def test_trang_chu(page):
    """Kiểm tra trang chủ load đúng, tiêu đề trang chính xác."""
    # 🔒 "page" là tham số bắt buộc viết đúng tên — pytest-playwright tự "tặng" công cụ này
    # giống hệt cách "mocker" hoạt động

    page.goto("https://automationexercise.com")
    page.keyboard.press("Escape")
    # ✏️ URL tự do, đây là hành động mở trang

    assert page.title() == "Automation Exercise"
    # 🔒 ".title()" là hàm có sẵn của Playwright, lấy tiêu đề trang web hiện tại
    # ✏️ chuỗi so sánh "Automation Exercise" 

def test_click_products(page):
    """Kiểm tra click vào menu Products điều hướng đúng trang."""
    page.goto("https://automationexercise.com")
    page.wait_for_timeout(1000)
    page.keyboard.press("Escape")

    # dòng code để click vào "Products" 
    # (dùng đúng cú pháp page.click("text=..."))
    page.click("text=Products", force=True)

    
    assert "products" in page.url

def test_dung_page_object(page):
    """Kiểm tra luồng mở trang + click Products hoạt động đúng qua Page Object Model."""
   
    trang_chu = HomePage(page)          #✏️ tạo object HomePage, truyền page vào

    # 2 dòng gọi hàm: mo_trang() và click_products()
    trang_chu.open_page()
    trang_chu.click_products()


    assert "products" in page.url    