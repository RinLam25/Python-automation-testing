from pages.login_page import LoginPage


def test_dang_nhap_sai_thong_tin(page):
    login_page = LoginPage(page)
    login_page.mo_trang()
    login_page.dang_nhap("khongtontai12345@gmail.com", "312sai")

    assert page.is_visible("text=Your email or password is incorrect!")

def test_dang_nhap_dung_thong_tin(page):
    login_page = LoginPage(page)
    login_page.mo_trang()
    login_page.dang_nhap("minhanh@gmail.com", "123456789minH")

    assert page.is_visible("text=Logged in as")