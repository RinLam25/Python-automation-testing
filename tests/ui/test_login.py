from pages.login_page import LoginPage


def test_dang_nhap_sai_thong_tin(page):
    """Kiểm tra hệ thống báo lỗi đúng khi đăng nhập sai thông tin."""
    login_page = LoginPage(page)
    login_page.mo_trang()
    login_page.dang_nhap("khongtontai12345@gmail.com", "312sai")

    assert page.is_visible("text=Your email or password is incorrect!")

def test_dang_nhap_dung_thong_tin(page):
    """Kiểm tra đăng nhập thành công với tài khoản hợp lệ.""" 
    login_page = LoginPage(page)
    login_page.mo_trang()
    login_page.dang_nhap("minhanh@gmail.com", "123456789minH")

    assert page.is_visible("text=Logged in as")

def test_dang_nhap_thieu_password(page):
    """Kiểm tra không thể đăng nhập khi bỏ trống trường Password."""
    login_page = LoginPage(page)
    login_page.mo_trang()
    login_page.dang_nhap("minhanh@gmail.com", "")

    assert "login" in page.url

def test_dang_nhap_email_khong_hop_le(page):
    """Kiểm tra đăng nhập với email sai định dạng."""
    login_page = LoginPage(page)
    login_page.mo_trang()
    login_page.dang_nhap("lamtherinnnnn", "123456")

    assert "login" in page.url

