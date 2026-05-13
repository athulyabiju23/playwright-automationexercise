from pages.base_page import BasePage


class SignupPage(BasePage):
    # initial signup form
    NAME_INPUT = "input[data-qa='signup-name']"
    EMAIL_INPUT = "input[data-qa='signup-email']"
    SIGNUP_BTN = "button[data-qa='signup-button']"
    SIGNUP_HEADING = "h2:has-text('New User Signup!')"

    EMAIL_EXISTS_ERROR = "text=Email Address already exist!"

    # account info form (shown after first signup click)
    TITLE_MR = "#id_gender1"
    PASSWORD_INPUT = "#password"
    DAY_DROPDOWN = "#days"
    MONTH_DROPDOWN = "#months"
    YEAR_DROPDOWN = "#years"

    # address info
    FIRST_NAME = "#first_name"
    LAST_NAME = "#last_name"
    COMPANY = "#company"
    ADDRESS = "#address1"
    COUNTRY = "#country"
    STATE = "#state"
    CITY = "#city"
    ZIPCODE = "#zipcode"
    MOBILE = "#mobile_number"

    CREATE_ACCOUNT_BTN = "button[data-qa='create-account']"
    ACCOUNT_CREATED_MSG = "h2[data-qa='account-created']"
    CONTINUE_BTN = "a[data-qa='continue-button']"

    def is_signup_section_visible(self):
        return self.is_visible(self.SIGNUP_HEADING)

    def enter_name_and_email(self, name, email):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.EMAIL_INPUT, email)

    def click_signup(self):
        self.click(self.SIGNUP_BTN)

    def is_email_exists_error_visible(self):
        return self.is_visible(self.EMAIL_EXISTS_ERROR)

    def fill_account_info(self, user):
        # use check() for radio - more reliable than click
        self.page.check(self.TITLE_MR)
        self.fill(self.PASSWORD_INPUT, user["password"])
        self.page.select_option(self.DAY_DROPDOWN, user["day"])
        self.page.select_option(self.MONTH_DROPDOWN, user["month"])
        self.page.select_option(self.YEAR_DROPDOWN, user["year"])

        self.fill(self.FIRST_NAME, user["first_name"])
        self.fill(self.LAST_NAME, user["last_name"])
        self.fill(self.COMPANY, user["company"])
        self.fill(self.ADDRESS, user["address"])
        self.page.select_option(self.COUNTRY, user["country"])
        self.fill(self.STATE, user["state"])
        self.fill(self.CITY, user["city"])
        self.fill(self.ZIPCODE, user["zipcode"])
        self.fill(self.MOBILE, user["mobile"])

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BTN)
        # wait for the account created page to load before continuing
        self.page.wait_for_url("**/account_created", timeout=15000)

    def is_account_created(self):
        return self.is_visible(self.ACCOUNT_CREATED_MSG)

    def click_continue_after_account_created(self):
        # after signup theres a Continue button - need to click it
        # to leave the account_created page
        self.click(self.CONTINUE_BTN)

    def signup_new_user(self, home_page):
        # helper - signs up a fresh user and returns their credentials
        # used by login tests so we have a real account to login with
        from utils.test_data import generate_user
        user = generate_user()

        home_page.click_signup_login()
        self.enter_name_and_email(user["name"], user["email"])
        self.click_signup()
        self.fill_account_info(user)
        self.click_create_account()
        self.click_continue_after_account_created()

        return user