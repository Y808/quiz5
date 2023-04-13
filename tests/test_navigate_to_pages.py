from pages.home_page import HomePage
from pages.settings_page import SettingsPage
from tests.data import strings


def test_navigate_back(init_driver, main_user_login):
    home_page = HomePage(init_driver)
    home_page.open_settings_page()
    settings_page = SettingsPage(init_driver)
    settings_page_header = settings_page.get_header_text()
    assert settings_page_header == strings.settings_header, "not settings page header"
    init_driver.back()
    assert home_page.get_your_feed_tab().is_enabled(), "not settings page header"


def test_navigate_forward(init_driver, main_user_login):
    home_page = HomePage(init_driver)
    home_page.open_settings_page()
    settings_page = SettingsPage(init_driver)
    settings_page_header = settings_page.get_header_text()
    assert settings_page_header == strings.settings_header, "not settings page header"
    init_driver.back()
    assert home_page.get_your_feed_tab().is_enabled(), "not settings page header"
    init_driver.forward()
    assert settings_page_header == strings.settings_header, "not settings page header after forward"
