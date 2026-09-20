class SignupPage:
    def __init__(self, page):
        self.page = page

    def mo_trang_login(self):
        self.page.goto("https://automationexercise.com/login")

    def dang_ky(self, ten, email):
        # 1. Gõ "ten" vào ô có data-qa="signup-name"
        self.page.fill('[data-qa="signup-name"]', ten)
        # 2. Gõ "email" vào ô có data-qa="signup-email"
        self.page.fill('[data-qa="signup-email"]', email)
        # 3. Click vào nút có data-qa="signup-button"
        self.page.click('[data-qa="signup-button"]', force=True)
