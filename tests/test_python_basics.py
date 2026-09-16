# Biến và kiểu dữ liệu
def test_variables():
    ten_san_pham = "Áo thun"      # string
    gia = 150000                   # int
    con_hang = True                # bool
    assert isinstance(ten_san_pham, str)

# List (danh sách) — dùng nhiều khi lưu danh sách sản phẩm
def test_list():
    danh_sach_san_pham = ["Áo thun", "Quần jean", "Giày"]
    assert len(danh_sach_san_pham) == 3
    assert danh_sach_san_pham[0] == "Áo thun"

# Dict (giống JSON) — dùng nhiều khi làm việc với response API
def test_dict():
    san_pham = {"ten": "Áo thun", "gia": 150000, "con_hang": True}
    assert san_pham["ten"] == "Áo thun"
    assert san_pham["gia"] == 150000

# Hàm (function)
def tinh_tong_gia(gia, so_luong):
    return gia * so_luong

def test_ham():
    assert tinh_tong_gia(150000, 2) == 300000

# Class cơ bản — nền tảng cho Page Object Model sau này
class SanPham:
    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia

    def hien_thi(self):
        return f"{self.ten}: {self.gia}đ"

def test_class():
    ao = SanPham("Áo thun", 150000)
    assert ao.hien_thi() == "Áo thun: 150000đ"