from pages.home_page import HomePage

def test_trang_chu(page):
    # 🔒 "page" là tham số bắt buộc viết đúng tên — pytest-playwright tự "tặng" công cụ này
    # giống hệt cách "mocker" hoạt động

    page.goto("https://automationexercise.com")
    page.keyboard.press("Escape")
    # ✏️ URL tự do, đây là hành động mở trang

    assert page.title() == "Automation Exercise"
    # 🔒 ".title()" là hàm có sẵn của Playwright, lấy tiêu đề trang web hiện tại
    # ✏️ chuỗi so sánh "Automation Exercise" 

def test_click_products(page):
    page.goto("https://automationexercise.com")
    page.keyboard.press("Escape")

    # dòng code để click vào "Products" 
    # (dùng đúng cú pháp page.click("text=..."))
    page.click("text=Products", force=True)

    # ✏️ Sau khi click, URL của trang sẽ đổi thành .../products
    # Playwright có sẵn: page.url  (không cần dấu ngoặc, đây là THUỘC TÍNH, không phải hàm)
    # viết 1 dòng assert để kiểm tra "products" có nằm trong page.url hay không
    # Gợi ý cú pháp kiểm tra 1 chuỗi có nằm TRONG 1 chuỗi khác: "abc" in "xabcx" → True
    assert "products" in page.url

def test_dung_page_object(page):
    
    #Lưu ý: test này có thể fail ngẫu nhiên (~20%) do quảng cáo Google Vignette 
    #tự động xuất hiện trên trang demo, không phải lỗi logic. 
    #Đã xử lý giảm thiểu bằng wait_for_timeout + Escape + force click.
   
    trang_chu = HomePage(page)          #✏️ tạo object HomePage, truyền page vào

    # 2 dòng gọi hàm: mo_trang() và click_products()
    trang_chu.open_page()
    trang_chu.click_products()
    # (không viết page.goto/page.click trực tiếp nữa, mà gọi qua trang_chu)

    assert "products" in page.url    