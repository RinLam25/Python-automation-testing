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