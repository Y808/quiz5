from os import wait

import pytest
import configs
from pages.signup_page import SignupPage
import time

from tests.conftest import read_strings_xml


def test_username_is_already_present_signup(init_driver, read_login_users):
    signup_page = SignupPage(init_driver)
    signup_page.open_signup_page()

    username = read_login_users["takenUserName"]["username"]
    email = read_login_users["takenUserName"]["email"]
    password = read_login_users["takenUserName"]["password"]
    signup_page.signup(username, email, password)
    assert signup_page.get_taken_username_error_text() == read_strings_xml()['taken_username']


def test_blank_username(init_driver, read_login_users):
    signup_page = SignupPage(init_driver)
    signup_page.open_signup_page()

    username = " "
    email = read_login_users["takenUserName"]["email"]
    password = read_login_users["takenUserName"]["password"]
    signup_page.signup(username, email, password)
    assert signup_page.get_taken_username_error_text() == read_strings_xml()['blank_username']


def test_blank_username(init_driver, read_login_users):
    signup_page = SignupPage(init_driver)
    signup_page.open_signup_page()

    username = " "
    email = read_login_users["takenUserName"]["email"]
    password = read_login_users["takenUserName"]["password"]
    signup_page.signup(username, email, password)
    assert signup_page.get_taken_username_error_text() == read_strings_xml()['blank_username']


def test_blank_password(init_driver, read_login_users):
    signup_page = SignupPage(init_driver)
    signup_page.open_signup_page()

    username = read_login_users["correctUserNameEmailPasswordForSignup"]["username"]
    email = read_login_users["correctUserNameEmailPasswordForSignup"]["email"]
    password = ""
    signup_page.signup(username, email, password)
    assert signup_page.get_password_error_text() == read_strings_xml()['blank_password']


def test_successful_signup(init_driver, read_login_users):
    signup_page = SignupPage(init_driver)
    signup_page.open_signup_page()

    username = read_login_users["correctUserNameEmailPasswordForSignup"]["username"]
    email = read_login_users["correctUserNameEmailPasswordForSignup"]["email"]
    password = read_login_users["correctUserNameEmailPasswordForSignup"]["password"]
    signup_page.signup(username, email, password)
    time.sleep(4)
    #assert that homepage is opened

