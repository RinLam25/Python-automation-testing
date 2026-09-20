import time
from pages.signup_page import SignupPage


def test_dang_ky_thanh_cong(page):
    signup_page = SignupPage(page)
    signup_page.mo_trang_login()

    email_ngau_nhien = f"rin{int(time.time())}@gmail.com"
    # 🔒 "time.time()" là hàm có sẵn của Python, trả về số giây hiện tại (dạng số thập phân)
    # "int(...)" chuyển nó thành số nguyên (bỏ phần thập phân)
    # → mỗi lần chạy test, số này sẽ khác nhau (vì thời gian luôn trôi), nên email luôn khác nhau

    signup_page.dang_ky("Rin Test", email_ngau_nhien)

    assert "signup" in page.url
  