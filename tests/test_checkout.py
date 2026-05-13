import pytest
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def logged_in_user_with_cart(page):
    # fixture - sets up a user thats logged in and has 1 item in cart
    # most checkout tests need this state so we share it
    home = HomePage(page)
    signup = SignupPage(page)
    login = LoginPage(page)
    products = ProductsPage(page)

    home.open()
    user = login.quick_login(home, signup)

    # add a product to cart
    products.open_products()
    products.add_first_product_to_cart()
    products.click_view_cart()

    return user


def test_checkout_requires_login(page):
    # user not logged in shouldnt be able to checkout
    # should see register/login prompt instead
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    products.open_products()
    products.add_first_product_to_cart()
    products.click_view_cart()
    cart.click_proceed_to_checkout()

    assert checkout.is_register_login_prompt_visible()


def test_checkout_shows_address_for_logged_in_user(logged_in_user_with_cart, page):
    # logged in user clicking checkout should see their address
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    cart.click_proceed_to_checkout()

    assert checkout.is_address_delivery_visible()
    assert checkout.is_review_order_visible()


def test_checkout_review_order_has_correct_items(logged_in_user_with_cart, page):
    # cart had 1 item, review order page should also show 1 item
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    cart.click_proceed_to_checkout()

    assert checkout.get_order_item_count() == 1


def test_complete_purchase_flow(logged_in_user_with_cart, page):
    # full happy path - logged in user completes a purchase
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    cart.click_proceed_to_checkout()
    checkout.add_comment("Please deliver fast thanks")
    checkout.click_place_order()

    checkout.fill_payment_info()
    checkout.click_pay()

    # wait for confirmation page
    page.wait_for_timeout(2000)

    assert checkout.is_order_placed()