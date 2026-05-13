# base page that all other pages inherit from
# common stuff goes here so we dont repeat it everywhere

class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = "https://automationexercise.com"

    def goto(self, path=""):
        self.page.goto(self.base_url + path)

    def get_title(self):
        return self.page.title()

    def is_visible(self, locator):
        return self.page.is_visible(locator)

    def click(self, locator):
        self.page.wait_for_selector(locator, state="visible", timeout=15000)
        self.page.click(locator)

    def fill(self, locator, text):
        self.page.fill(locator, text)