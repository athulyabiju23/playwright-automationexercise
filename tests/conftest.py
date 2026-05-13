import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    # runs before every test - fresh browser each time
    # set headless=False if u wanna watch the browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        pg = context.new_page()
        yield pg
        browser.close()