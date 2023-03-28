import time

import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
import configs
from pages.settings_page import SettingsPage
from tests.conftest import read_strings_xml, read_login_users


def test_change_password_and_bio(init_driver, read_login_users):
    login_page = LoginPage(init_driver)
    settings_page = SettingsPage(init_driver)
    home_page = HomePage(init_driver)
    login_page.open_login_page()
    email = read_login_users["validUser1"]["email"]
    password = read_login_users["validUser1"]["password"]
    login_page.login(email, password)
    time.sleep(2)
    settings_page.open_settings_page()
    time.sleep(2)
    password = "87654321"
    bio = "Hello world!"
    settings_page.change_password_and_bio(password, bio)
    assert read_login_users["validUser1"]["username"] == home_page.get_workspace_text()
    assert home_page.get_your_feed_tab().is_enabled()

def test_change_password_back(init_driver, read_login_users):
    login_page = LoginPage(init_driver)
    settings_page = SettingsPage(init_driver)
    home_page = HomePage(init_driver)
    login_page.open_login_page()
    email = read_login_users["validUser1"]["email"]
    password = "87654321"
    login_page.login(email, password)
    time.sleep(2)
    settings_page.open_settings_page()
    time.sleep(2)
    password = read_login_users["validUser1"]["password"]
    bio = "Hello world!"
    settings_page.change_password_and_bio(password, bio)
    assert read_login_users["validUser1"]["username"] == home_page.get_workspace_text()
    assert home_page.get_your_feed_tab().is_enabled()
