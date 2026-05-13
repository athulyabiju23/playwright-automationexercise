from pages.base_page import BasePage


class HomePage(BasePage):
    # locators
    LOGO = "img[alt='Website for automation practice']"
    SIGNUP_LOGIN_BTN = "a[href='/login']"
    PRODUCTS_BTN = "a[href='/products']"
    CART_BTN = "a[href='/view_cart']"
    CONTACT_BTN = "a[href='/contact_us']"

    def open(self):
        self.goto("/")

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_BTN)

    def click_products(self):
        self.click(self.PRODUCTS_BTN)

    def click_cart(self):
        self.click(self.CART_BTN)

    def is_logo_visible(self):
        return self.is_visible(self.LOGO)