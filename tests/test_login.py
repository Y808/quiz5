import pytest
import requests
from helpers.utils import generate_random_credentials
from pages.login_page import LoginPage
from pages.home_page import HomePage
from tests.data import login_users, strings


def test_success_user_login(init_driver):
    login_page = LoginPage(init_driver)
    home_page = HomePage(init_driver)
    login_page.open_login_page()

    email = login_users.user1Email
    password = login_users.user1Password
    login_page.login(email, password)
    assert login_users.user1Username == home_page.get_workspace_text(), "username of logged in user do not to match workspace name"
    assert home_page.get_your_feed_tab().is_enabled(), "YOUR_FEED_TAB is not enabled"


def test_login_with_blank_password(init_driver):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()

    email = login_users.user1Email
    password = ""
    login_page.login_with_errors(email, password)
    assert login_page.get_password_error_text() == strings.login_blank_password


def test_login_with_blank_email(init_driver):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()

    email = ""
    password = login_users.user1Password
    login_page.login_with_errors(email, password)
    assert login_page.get_email_error_text() == strings.login_blank_email, "not blank email error"


def test_login_with_blank_email_and_password(init_driver, read_login_users):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()

    email = ""
    password = ""
    login_page.login_with_errors(email, password)
    assert login_page.get_email_error_text() == strings.login_blank_email, "not blank email error"


def test_username_instead_email(init_driver):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()

    email = login_users.user1Username
    password = login_users.user1Password
    login_page.login_with_errors(email, password)

    error_message = init_driver.execute_script("return document.querySelector('input["
                                               "type=email]:invalid').validationMessage;")
    assert strings.js_email_error in error_message, "not incorrect email error"


@pytest.fixture
def test_signup_with_api(init_driver):
    # Sign up a new user using API
    random_cred = generate_random_credentials()
    user = {
        'email': random_cred['email'],
        'password': random_cred['password'],
        'username': random_cred['username']
    }
    response = requests.post('https://api.realworld.io/api/users', json=user)
    print(response.content)
    assert response.status_code == 200, f"Failed to sign up user with API. Response code: {response.status_code}"

    # Test login with UI
    login_page = LoginPage(init_driver)
    home_page = HomePage(init_driver)
    login_page.open_login_page()
    login_page.login(random_cred['email'], random_cred['password'])
    home_page.wait_until_page_is_loaded()

    assert random_cred[
               'username'] == home_page.get_workspace_text(), "username on signup is not the same as on workspace"
    assert home_page.get_your_feed_tab().is_enabled(), "YOUR_FEED_TAB is not enabled"
