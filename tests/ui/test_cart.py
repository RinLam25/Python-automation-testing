from pages.cart_page import CartPage


def test_them_san_pham_vao_gio(page):
    cart_page = CartPage(page)
    cart_page.mo_trang_san_pham()
    cart_page.them_san_pham_dau_tien_vao_gio()
    cart_page.xem_gio_hang()

    assert "view_cart" in page.url
    assert page.is_visible("text=Shopping Cart")
