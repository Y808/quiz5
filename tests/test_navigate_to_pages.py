import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from tests.data import strings


@pytest.fixture(scope="function")
def login_user(init_driver, read_login_users):
    login_page = LoginPage(init_driver)
    email = read_login_users["validUser1"]["email"]
    password = read_login_users["validUser1"]["password"]
    login_page.open_login_page()
    login_page.login(email, password)
    yield email, password


def test_navigate_back(init_driver, login_user):
    home_page = HomePage(init_driver)
    home_page.open_settings_page()
    settings_page = SettingsPage(init_driver)
    settings_page_header = settings_page.get_header_text()
    assert settings_page_header == strings.settings_header
    init_driver.back()
    assert home_page.get_your_feed_tab().is_enabled()


def test_navigate_forward(init_driver, login_user):
    home_page = HomePage(init_driver)
    home_page.open_settings_page()
    settings_page = SettingsPage(init_driver)
    settings_page_header = settings_page.get_header_text()
    assert settings_page_header == strings.settings_header
    init_driver.back()
    assert home_page.get_your_feed_tab().is_enabled()
    init_driver.forward()
    assert settings_page_header == strings.settings_header
