from pages.base_page import BasePage


class ProductsPage(BasePage):
    # locators
    SEARCH_INPUT = "#search_product"
    SEARCH_BTN = "#submit_search"
    PRODUCTS_LIST = ".features_items"
    SEARCHED_PRODUCTS_HEADING = "h2:has-text('Searched Products')"
    PRODUCT_CARDS = ".product-image-wrapper"

    # for adding first product to cart
    FIRST_PRODUCT_ADD_BTN = ".product-image-wrapper:first-child .add-to-cart"
    CONTINUE_SHOPPING_BTN = "button:has-text('Continue Shopping')"
    VIEW_CART_LINK = "u:has-text('View Cart')"

    def open_products(self):
        self.goto("/products")

    def search_product(self, name):
        self.fill(self.SEARCH_INPUT, name)
        self.click(self.SEARCH_BTN)

    def is_searched_products_visible(self):
        return self.is_visible(self.SEARCHED_PRODUCTS_HEADING)

    def get_product_count(self):
        # returns how many product cards are visible
        return self.page.locator(self.PRODUCT_CARDS).count()

    def add_first_product_to_cart(self):
        # hover first product then click add to cart
        first_product = self.page.locator(self.PRODUCT_CARDS).first
        first_product.hover()
        # click the add to cart button that appears on hover
        self.page.locator(".product-overlay .add-to-cart").first.click()

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def click_view_cart(self):
        self.click(self.VIEW_CART_LINK)