from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_products_page_loads(page):
    # check we can navigate to products page and see items
    home = HomePage(page)
    products = ProductsPage(page)

    home.open()
    products.open_products()

    # at least some products should show up
    assert products.get_product_count() > 0


def test_search_product(page):
    # search for a known product and check results
    products = ProductsPage(page)

    products.open_products()
    products.search_product("dress")

    assert products.is_searched_products_visible()
    # should find at least one matching product
    assert products.get_product_count() > 0


def test_add_product_to_cart(page):
    # add first product, then check cart has 1 item
    products = ProductsPage(page)
    cart = CartPage(page)

    products.open_products()
    products.add_first_product_to_cart()
    products.click_view_cart()

    assert cart.get_item_count() == 1


def test_remove_product_from_cart(page):
    # add a product then remove it - cart should be empty
    products = ProductsPage(page)
    cart = CartPage(page)

    products.open_products()
    products.add_first_product_to_cart()
    products.click_view_cart()

    assert cart.get_item_count() == 1

    cart.delete_first_item()
    # wait a sec for the item to actually be removed
    page.wait_for_timeout(1000)

    assert cart.is_cart_empty()


def test_cart_persists_after_navigation(page):
    # add product, navigate away, come back - item should still be there
    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    products.open_products()
    products.add_first_product_to_cart()
    products.click_continue_shopping()

    # navigate back to home
    home.open()

    # then go to cart
    cart.open_cart()

    assert cart.get_item_count() == 1