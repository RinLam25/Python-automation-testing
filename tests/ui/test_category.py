def test_filter_theo_category(page):
    page.goto("https://automationexercise.com/products")
    page.wait_for_timeout(1000)
    page.keyboard.press("Escape")

    page.click("text=Women", force=True)
    page.wait_for_timeout(500)   # chờ accordion "Women" kịp mở ra trước khi click "Dress"
    page.click('a[href="/category_products/1"]', force=True)

    assert "category_products/1" in page.url

def test_filter_category_tops(page):
    """Kiểm tra filter category Tops trả đúng URL và hiển thị đúng trang."""
    page.goto("https://automationexercise.com/products")
    page.click("text=Women", force=True)
    page.wait_for_timeout(500)
    page.click('a[href="/category_products/2"]', force=True)

    assert "category_products/2" in page.url

def test_tim_kiem_san_pham_khong_ton_tai(page):
    """Kiểm tra tìm kiếm với từ khóa không tồn tại trả về danh sách rỗng."""
    page.goto("https://automationexercise.com/products")
    page.fill("#search_product", "123biugba")
    page.click("#submit_search", force=True)

    san_pham_tim_thay = page.locator(".productinfo").all()
    assert len(san_pham_tim_thay) == 0

def test_filter_category_saree(page):
    """Kiểm tra filter category Saree trả đúng URL và hiển thị đúng trang."""
    page.goto("https://automationexercise.com/products")
    page.click("text=Women", force=True)
    page.wait_for_timeout(500)
    page.click('a[href="/category_products/7"]', force=True)

    assert "category_products/7" in page.url

def test_filter_category_tshirts(page):
    """Kiểm tra filter category t_shirts trả đúng URL và hiển thị đúng trang."""
    page.goto("https://automationexercise.com/products")
    page.click('a[href="#Men"]', force=True)
    page.wait_for_timeout(1000)
    page.click('a[href="/category_products/3"]', force=True)

    assert "category_products/3" in page.url

def test_filter_category_jeans(page):
    """Kiểm tra filter category jeans trả đúng URL và hiển thị đúng trang."""
    page.goto("https://automationexercise.com/products")
    page.click('a[href="#Men"]', force=True)
    page.wait_for_timeout(1000)
    page.click('a[href="/category_products/6"]', force=True)

    assert "category_products/6" in page.url

def test_tim_kiem_voi_khoang_trang(page):
    """Kiểm tra tìm kiếm chỉ với dấu cách, không có nội dung thật."""
    page.goto("https://automationexercise.com/products")
    page.fill("#search_product", "   ")
    page.click("#submit_search", force=True)

def test_tim_kiem_tieng_viet_co_dau(page):
    """Kiểm tra tìm kiếm với ký tự tiếng Việt có dấu không làm crash trang."""
    page.goto("https://automationexercise.com/products")
    page.fill("#search_product", "áo thun")
    page.click("#submit_search", force=True)

    assert "search=" in page.url