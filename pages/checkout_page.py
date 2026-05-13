from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # delivery + billing address sections show on checkout page
    ADDRESS_DELIVERY = "#address_delivery"
    ADDRESS_INVOICE = "#address_invoice"

    # order review section
    REVIEW_ORDER_HEADING = "h2:has-text('Review Your Order')"
    CART_ITEMS = "#cart_info tr.cart_product, tr[id^='product-']"

    # comment + place order
    COMMENT_BOX = "textarea.form-control"
    PLACE_ORDER_BTN = "a:has-text('Place Order')"

    # payment form
    NAME_ON_CARD = "input[data-qa='name-on-card']"
    CARD_NUMBER = "input[data-qa='card-number']"
    CVC = "input[data-qa='cvc']"
    EXPIRY_MONTH = "input[data-qa='expiry-month']"
    EXPIRY_YEAR = "input[data-qa='expiry-year']"
    PAY_BTN = "button[data-qa='pay-button']"

    # success
    ORDER_PLACED_MSG = "p:has-text('Congratulations! Your order has been confirmed!')"

    # login required popup (shows if user clicks checkout while logged out)
    REGISTER_LOGIN_LINK = "u:has-text('Register / Login')"

    def is_address_delivery_visible(self):
        return self.is_visible(self.ADDRESS_DELIVERY)

    def is_review_order_visible(self):
        return self.is_visible(self.REVIEW_ORDER_HEADING)

    def get_order_item_count(self):
        return self.page.locator(self.CART_ITEMS).count()

    def add_comment(self, text):
        self.fill(self.COMMENT_BOX, text)

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BTN)
        # wait for payment page to load
        self.page.wait_for_url("**/payment", timeout=15000)

    def fill_payment_info(self):
        # using fake test card info - this is a demo site so doesnt matter
        self.fill(self.NAME_ON_CARD, "Test User")
        self.fill(self.CARD_NUMBER, "4111111111111111")
        self.fill(self.CVC, "123")
        self.fill(self.EXPIRY_MONTH, "12")
        self.fill(self.EXPIRY_YEAR, "2028")

    def click_pay(self):
        self.click(self.PAY_BTN)

    def is_order_placed(self):
        return self.is_visible(self.ORDER_PLACED_MSG)

    def is_register_login_prompt_visible(self):
        # this shows when user tries to checkout without being logged in
        return self.is_visible(self.REGISTER_LOGIN_LINK)