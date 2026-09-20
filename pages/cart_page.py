class CartPage:
    def __init__(self, page):
        self.page = page

    def mo_trang_san_pham(self):
        self.page.goto("https://automationexercise.com/products")

    def them_san_pham_dau_tien_vao_gio(self):
        self.page.click('a[data-product-id="1"]', force=True)
        self.page.wait_for_timeout(1000)
        # ✏️ số "1" là ID của sản phẩm đầu tiên trên trang — bạn có thể Inspect để xác nhận

    def xem_gio_hang(self):
        self.page.click("text=View Cart", force=True)

    def xoa_san_pham_khoi_gio(self):
        nut_xoa = self.page.locator(".cart_quantity_delete")
        nut_xoa.scroll_into_view_if_needed()   # ✏️ chủ động cuộn tới, không phó mặc cho click tự lo
        self.page.wait_for_timeout(500)
        nut_xoa.click(force=True)
        self.page.wait_for_timeout(1000)