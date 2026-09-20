class LoginPage:
    def __init__(self, page):
        self.page = page

    def mo_trang(self):
        self.page.goto("https://automationexercise.com/login")

    def dang_nhap(self, email, password):
        self.page.fill('[data-qa="login-email"]', email)
        self.page.fill('[data-qa="login-password"]', password)
        self.page.click('[data-qa="login-button"]', force=True)