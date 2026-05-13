import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


@pytest.fixture
def registered_user(page):
    # creates a fresh user before login tests run
    # this way we always have a valid account to test against
    home = HomePage(page)
    signup = SignupPage(page)

    home.open()
    user = signup.signup_new_user(home)

    # logout after signup so we can test login fresh
    login = LoginPage(page)
    login.logout()

    return user


def test_login_with_valid_credentials(registered_user, page):
    # happy path - registered user can log in
    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_signup_login()

    assert login.is_login_section_visible()

    login.login(registered_user["email"], registered_user["password"])

    assert login.is_user_logged_in()


def test_login_with_wrong_password(registered_user, page):
    # login should fail when password is wrong
    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_signup_login()

    login.login(registered_user["email"], "WrongPassword123!")

    assert login.is_login_error_visible()


def test_login_with_unregistered_email(page):
    # login should fail with email that was never registered
    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_signup_login()

    login.login("notregistered_xyz@testmail.com", "SomePassword@1")

    assert login.is_login_error_visible()


def test_login_with_empty_fields(page):
    # login button shouldnt work with empty fields
    # the html required attr stops form submission
    home = HomePage(page)
    login = LoginPage(page)

    home.open()
    home.click_signup_login()

    # dont fill anything just click
    page.click(login.LOGIN_BTN)

    # we should still be on the login section
    assert login.is_login_section_visible()