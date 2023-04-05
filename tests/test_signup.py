from pages.home_page import HomePage
from pages.signup_page import SignupPage
from tests.data import strings
from helpers.utils import *


def test_username_is_already_present_signup(init_driver, read_login_users):
    signup_page = SignupPage(init_driver)
    signup_page.open_signup_page()

    username = read_login_users["takenUserName"]["username"]
    email = read_login_users["takenUserName"]["email"]
    password = read_login_users["takenUserName"]["password"]
    signup_page.signup(username, email, password)
    assert signup_page.get_taken_username_error_text() == strings.taken_username


def test_blank_username(init_driver, read_login_users):
    signup_page = SignupPage(init_driver)
    signup_page.open_signup_page()

    username = ""
    email = read_login_users["takenUserName"]["email"]
    password = read_login_users["takenUserName"]["password"]
    signup_page.signup(username, email, password)
    assert signup_page.get_taken_username_error_text() == strings.blank_username


def test_blank_email(init_driver, read_login_users):
    signup_page = SignupPage(init_driver)
    signup_page.open_signup_page()

    username = read_login_users["takenUserName"]["username"]
    email = ""
    password = read_login_users["takenUserName"]["password"]
    signup_page.signup(username, email, password)
    assert signup_page.get_email_error_text() == strings.blank_email


def test_blank_password(init_driver, read_login_users):
    signup_page = SignupPage(init_driver)
    signup_page.open_signup_page()

    username = read_login_users["correctUserNameEmailPasswordForSignup"]["username"]
    email = read_login_users["correctUserNameEmailPasswordForSignup"]["email"]
    password = ""
    signup_page.signup(username, email, password)
    assert signup_page.get_password_error_text() == strings.blank_password


def test_successful_signup(init_driver, read_login_users):
    signup_page = SignupPage(init_driver)
    home_page = HomePage(init_driver)
    signup_page.open_signup_page()

    random_cred = generate_random_credentials()
    username = random_cred['username']
    email = random_cred['email']
    password = random_cred['password']
    signup_page.signup(username, email, password)

    assert random_cred['username'] == home_page.get_workspace_text()
    assert home_page.get_your_feed_tab().is_enabled()
