import datetime
import time

import pytest

from pages.article_page import ArticlePage
from pages.create_article_page import NewArticlePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from tests.conftest import read_strings_xml


@pytest.fixture(scope="function")
def login_user(init_driver, read_login_users):
    login_page = LoginPage(init_driver)
    email = read_login_users["validUser1"]["email"]
    password = read_login_users["validUser1"]["password"]
    login_page.open_login_page()
    login_page.login(email, password)
    yield email, password


def test_mark_article_as_favourite(init_driver, login_user):
    home_page = HomePage(init_driver)
    profile_page = ProfilePage(init_driver)
    home_page.open_global_feed_tab()
    likes_before_click = home_page.get_number_of_last_article_likes()
    time.sleep(2)
    home_page.click_on_heard_icon_on_last_article()
    time.sleep(5)
    article_title = home_page.get_last_article_title()
    assert home_page.get_number_of_last_article_likes() == likes_before_click + 1

    profile_page.open_profile_page()
    profile_page.open_favourite_tab()

    assert article_title == profile_page.get_first_article_title()


def test_unmark_article_as_favourite(init_driver, login_user):
    home_page = HomePage(init_driver)
    profile_page = ProfilePage(init_driver)
    home_page.open_global_feed_tab()
    likes_before_click = home_page.get_number_of_last_article_likes()
    time.sleep(2)
    home_page.click_on_heard_icon_on_last_article()
    time.sleep(5)
    assert home_page.get_number_of_last_article_likes() == likes_before_click - 1


def test_mark_multiple_article_as_favourite(init_driver, login_user):
    home_page = HomePage(init_driver)
    profile_page = ProfilePage(init_driver)
    home_page.open_global_feed_tab()
    likes_before_click1 = home_page.get_number_of_second_last_article_likes()
    likes_before_click2 = home_page.get_number_of_last_article_likes()
    time.sleep(2)
    home_page.click_on_heard_icon_on_last_article()
    home_page.click_on_heard_icon_on_second_last_article()
    time.sleep(5)

    assert home_page.get_number_of_second_last_article_likes() == likes_before_click1 + 1
    assert home_page.get_number_of_last_article_likes() == likes_before_click2 + 1


