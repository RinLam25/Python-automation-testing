class HomePage:
    def __init__(self, page):
        self.page = page

    def open_page(self):
        self.page.goto("https://automationexercise.com")
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("Escape")

    def click_products(self):
        self.page.click("text=Products", force=True)

