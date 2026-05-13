from pages.home_page import HomePage


def test_homepage_loads(page):
    # smoke test - just checks homepage loads
    home = HomePage(page)
    home.open()

    assert "Automation Exercise" in home.get_title()
    assert home.is_logo_visible()