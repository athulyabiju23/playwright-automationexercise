from pages.base_page import BasePage


class CartPage(BasePage):
    # locators
    CART_TABLE = "#cart_info_table"
    CART_ITEMS = "#cart_info_table tbody tr"
    EMPTY_CART_MSG = "#empty_cart"
    PROCEED_TO_CHECKOUT_BTN = ".btn.btn-default.check_out"

    # for each cart item
    DELETE_BTN = ".cart_quantity_delete"
    QUANTITY = ".cart_quantity_input"
    PRICE = ".cart_price"

    def open_cart(self):
        self.goto("/view_cart")

    def get_item_count(self):
        return self.page.locator(self.CART_ITEMS).count()

    def is_cart_empty(self):
        return self.is_visible(self.EMPTY_CART_MSG)

    def get_first_item_quantity(self):
        return self.page.locator(self.QUANTITY).first.input_value()

    def delete_first_item(self):
        self.page.locator(self.DELETE_BTN).first.click()

    def click_proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BTN)