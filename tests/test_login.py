from pages.login_page import LoginPage
from pages.home_page import HomePage
from tests.conftest import read_strings_xml
from tests.data import login_users, strings


def test_success_user_login(init_driver):
    login_page = LoginPage(init_driver)
    home_page = HomePage(init_driver)
    login_page.open_login_page()

    email = login_users.user1Email
    password = login_users.user1Password
    login_page.login(email, password)
    assert login_users.user1Username == home_page.get_workspace_text()
    assert home_page.get_your_feed_tab().is_enabled()


def test_login_with_blank_password(init_driver):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()

    email = login_users.user1Email
    password = ""
    login_page.login(email, password)
    assert login_page.get_password_error_text() == strings.login_blank_password


def test_login_with_blank_email(init_driver):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()

    email = ""
    password = login_users.user1Password
    login_page.login(email, password)
    assert login_page.get_email_error_text() == strings.login_blank_email


def test_login_with_blank_email_and_password(init_driver, read_login_users):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()

    email = ""
    password = ""
    login_page.login(email, password)
    assert login_page.get_email_error_text() == strings.login_blank_email


def test_username_instead_email(init_driver, read_login_users):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()

    email = login_users.user1Username
    password = login_users.user1Password
    login_page.login(email, password)

    error_message = init_driver.execute_script("return document.querySelector('input["
                                               "type=email]:invalid').validationMessage;")
    assert read_strings_xml()['js_email_error'] in error_message
