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
