import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    # fresh browser per test
    # blocking ads at network level cuz the site has google vignette popups
    # that block our clicks and break tests
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        pg = context.new_page()

        # block ads / analytics / trackers - they slow tests + cause popups
        pg.route("**/*", lambda route: (
            route.abort()
            if any(blocked in route.request.url for blocked in [
                "googlesyndication.com",
                "googletagmanager.com",
                "google-analytics.com",
                "doubleclick.net",
                "googleadservices.com",
                "adservice.google.com",
                "facebook.com",
                "facebook.net",
            ])
            else route.continue_()
        ))

        yield pg
        browser.close()