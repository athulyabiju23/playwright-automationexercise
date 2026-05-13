from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.test_data import generate_user


def test_signup_with_valid_data(page):
    # happy path - new user can sign up successfully
    home = HomePage(page)
    signup = SignupPage(page)
    user = generate_user()

    home.open()
    home.click_signup_login()

    assert signup.is_signup_section_visible()

    signup.enter_name_and_email(user["name"], user["email"])
    signup.click_signup()

    signup.fill_account_info(user)
    signup.click_create_account()

    assert signup.is_account_created()


def test_signup_with_existing_email(page):
    # signup should fail when email already registered
    # we sign up once, logout, then try again with same email
    from pages.login_page import LoginPage
    home = HomePage(page)
    signup = SignupPage(page)
    login = LoginPage(page)
    user = generate_user()

    # first signup - should work
    home.open()
    home.click_signup_login()
    signup.enter_name_and_email(user["name"], user["email"])
    signup.click_signup()
    signup.fill_account_info(user)
    signup.click_create_account()
    signup.click_continue_after_account_created()

    # logout so signup_login button is visible again
    login.logout()

    # second signup with same email - should fail
    home.open()
    home.click_signup_login()
    signup.enter_name_and_email(user["name"], user["email"])
    signup.click_signup()

    assert signup.is_email_exists_error_visible()
    
def test_signup_empty_fields(page):
    # signup should not proceed when name and email are empty
    home = HomePage(page)
    signup = SignupPage(page)

    home.open()
    home.click_signup_login()

    # dont fill anything just click
    signup.click_signup()

    # we should still be on signup section (browser blocks the form via required attribute)
    assert signup.is_signup_section_visible()