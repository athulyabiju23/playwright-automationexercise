from pages.base_page import BasePage


class LoginPage(BasePage):
    # locators - login form is on same page as signup but diff section
    LOGIN_HEADING = "h2:has-text('Login to your account')"
    EMAIL_INPUT = "input[data-qa='login-email']"
    PASSWORD_INPUT = "input[data-qa='login-password']"
    LOGIN_BTN = "button[data-qa='login-button']"

    # error message for wrong creds
    LOGIN_ERROR = "text=Your email or password is incorrect!"

    # after successful login
    LOGGED_IN_AS = "a:has-text('Logged in as')"
    LOGOUT_BTN = "a[href='/logout']"

    def is_login_section_visible(self):
        return self.is_visible(self.LOGIN_HEADING)

    def login(self, email, password):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)

    def is_login_error_visible(self):
        return self.is_visible(self.LOGIN_ERROR)

    def is_user_logged_in(self):
        return self.is_visible(self.LOGGED_IN_AS)

    def logout(self):
        self.click(self.LOGOUT_BTN)

    def quick_login(self, home_page, signup_page):
        # helper - creates a fresh user, logs out, logs back in
        # used for checkout tests that need a logged-in user
        user = signup_page.signup_new_user(home_page)
        self.logout()

        home_page.click_signup_login()
        self.login(user["email"], user["password"])

        return user