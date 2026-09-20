def test_input_email_co_placeholder(page):
    """Kiểm tra ô nhập email ở trang login/signup có placeholder hướng dẫn người dùng."""
    page.goto("https://automationexercise.com/login")

    placeholder_signup = page.get_attribute('[data-qa="signup-email"]', "placeholder")
    placeholder_login = page.get_attribute('[data-qa="login-email"]', "placeholder")

    assert placeholder_signup is not None and placeholder_signup != ""
    assert placeholder_login is not None and placeholder_login != ""