import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from tests.data import strings, login_users


@pytest.fixture(scope="function")
def login_user(init_driver):
    login_page = LoginPage(init_driver)
    email = login_users.user1Email
    password = login_users.user1Password
    login_page.open_login_page()
    login_page.login(email, password)
    home_page = HomePage(init_driver)
    home_page.wait_until_page_is_loaded()
    yield email, password


def test_navigate_back(init_driver, login_user):
    home_page = HomePage(init_driver)
    home_page.open_settings_page()
    settings_page = SettingsPage(init_driver)
    settings_page_header = settings_page.get_header_text()
    assert settings_page_header == strings.settings_header, "not settings page header"
    init_driver.back()
    assert home_page.get_your_feed_tab().is_enabled(), "not settings page header"


def test_navigate_forward(init_driver, login_user):
    home_page = HomePage(init_driver)
    home_page.open_settings_page()
    settings_page = SettingsPage(init_driver)
    settings_page_header = settings_page.get_header_text()
    assert settings_page_header == strings.settings_header, "not settings page header"
    init_driver.back()
    assert home_page.get_your_feed_tab().is_enabled(), "not settings page header"
    init_driver.forward()
    assert settings_page_header == strings.settings_header, "not settings page header after forward"
