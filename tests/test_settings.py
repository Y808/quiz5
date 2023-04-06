import time
from helpers.utils import generate_random_string
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.settings_page import SettingsPage
from tests.data import login_users


def test_change_password(init_driver):
    login_page = LoginPage(init_driver)
    settings_page = SettingsPage(init_driver)
    home_page = HomePage(init_driver)
    login_page.open_login_page()
    email = login_users.user1Email
    password = login_users.user1Password
    login_page.login(email, password)
    time.sleep(2)
    settings_page.open_settings_page()
    time.sleep(2)
    password = "87654321"
    settings_page.change_password(password)
    assert login_users.user1Username == home_page.get_workspace_text()
    assert home_page.get_your_feed_tab().is_enabled()
    settings_page.open_settings_page()
    time.sleep(2)
    settings_page.logout()
    login_page.open_login_page()
    login_page.login(email, password)
    time.sleep(2)
    settings_page.open_settings_page()
    time.sleep(2)
    password = "12345678"
    settings_page.change_password(password)
    assert login_users.user1Username == home_page.get_workspace_text()
    assert home_page.get_your_feed_tab().is_enabled()


def test_change_bio(init_driver):
    login_page = LoginPage(init_driver)
    settings_page = SettingsPage(init_driver)
    home_page = HomePage(init_driver)
    login_page.open_login_page()
    email = login_users.user1Email
    password = login_users.user1Password
    login_page.login(email, password)
    time.sleep(2)
    settings_page.open_settings_page()
    bio_before = settings_page.get_bio_text()
    time.sleep(2)
    bio = generate_random_string()
    settings_page.change_bio(bio)
    assert login_users.user1Username == home_page.get_workspace_text()
    assert home_page.get_your_feed_tab().is_enabled()
    assert bio_before != bio
