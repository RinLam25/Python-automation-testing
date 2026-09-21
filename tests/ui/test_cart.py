from pages.cart_page import CartPage


def test_them_san_pham_vao_gio(page):
    """Kiểm tra thêm sản phẩm vào giỏ hàng thành công."""
    cart_page = CartPage(page)
    cart_page.mo_trang_san_pham()
    cart_page.them_san_pham_dau_tien_vao_gio()
    cart_page.xem_gio_hang()

    assert "view_cart" in page.url
    assert page.is_visible("text=Shopping Cart")

def test_xoa_san_pham_khoi_gio(page):
    """Kiểm tra sản phẩm biến mất khỏi giỏ hàng sau khi bấm nút xóa."""
    cart_page = CartPage(page)
    cart_page.mo_trang_san_pham()
    cart_page.them_san_pham_dau_tien_vao_gio()
    cart_page.xem_gio_hang()
    cart_page.xoa_san_pham_khoi_gio()

    assert page.is_visible("text=Cart is empty!")

def test_them_san_pham_khac_vao_gio(page):
    """Kiểm tra thêm sản phẩm thứ 2 vào giỏ hàng thành công."""
    cart_page = CartPage(page)
    cart_page.mo_trang_san_pham()
    page.click('a[data-product-id="2"]', force=True)
    page.wait_for_timeout(1000)
    cart_page.xem_gio_hang()

    assert "view_cart" in page.url