def test_input_email_co_placeholder(page):
    """Kiểm tra ô nhập email ở trang login/signup có placeholder hướng dẫn người dùng."""
    page.goto("https://automationexercise.com/login")

    placeholder_signup = page.get_attribute('[data-qa="signup-email"]', "placeholder")
    placeholder_login = page.get_attribute('[data-qa="login-email"]', "placeholder")

    assert placeholder_signup is not None and placeholder_signup != ""
    assert placeholder_login is not None and placeholder_login != ""

def test_tim_kiem_voi_khoang_trang(page):
    """Kiểm tra tìm kiếm chỉ với dấu cách, hệ thống coi như tìm kiếm rỗng."""
    page.goto("https://automationexercise.com/products")
    page.fill("#search_product", "   ")
    page.click("#submit_search", force=True)

    assert "search=" in page.url