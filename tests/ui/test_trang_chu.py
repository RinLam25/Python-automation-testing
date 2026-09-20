from pages.home_page import HomePage

def test_trang_chu(page):
    # 🔒 "page" là tham số bắt buộc viết đúng tên — pytest-playwright tự "tặng" công cụ này
    # giống hệt cách "mocker" hoạt động mà bạn đã quen

    page.goto("https://automationexercise.com")
    page.keyboard.press("Escape")
    # ✏️ URL tự do, đây là hành động mở trang

    assert page.title() == "Automation Exercise"
    # 🔒 ".title()" là hàm có sẵn của Playwright, lấy tiêu đề trang web hiện tại
    # ✏️ chuỗi so sánh "Automation Exercise" — bạn cần TỰ KIỂM TRA xem tiêu đề thật của trang là gì

def test_click_products(page):
    page.goto("https://automationexercise.com")
    page.keyboard.press("Escape")

    # ✏️ Bạn tự viết dòng code để click vào "Products" 
    # (dùng đúng cú pháp page.click("text=...") mình vừa giải thích)
    page.click("text=Products", force=True)

    # ✏️ Sau khi click, URL của trang sẽ đổi thành .../products
    # Playwright có sẵn: page.url  (không cần dấu ngoặc, đây là THUỘC TÍNH, không phải hàm)
    # Bạn tự viết 1 dòng assert để kiểm tra "products" có nằm trong page.url hay không
    # Gợi ý cú pháp kiểm tra 1 chuỗi có nằm TRONG 1 chuỗi khác: "abc" in "xabcx" → True
    assert "products" in page.url

def test_dung_page_object(page):
    trang_chu = HomePage(page)          #✏️ tạo object HomePage, truyền page vào

    # ✏️ Bạn tự viết 2 dòng gọi hàm: mo_trang() và click_products()
    trang_chu.open_page()
    trang_chu.click_products()
    # (không viết page.goto/page.click trực tiếp nữa, mà gọi qua trang_chu)

    assert "products" in page.url    