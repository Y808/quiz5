import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


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

    # Teardown step: unmark any articles marked as favorites during the test
    profile_page = ProfilePage(init_driver)
    profile_page.open_profile_page()
    profile_page.click_on_heart_icon()


def test_mark_article_as_favourite(init_driver, login_user):
    home_page = HomePage(init_driver)
    profile_page = ProfilePage(init_driver)
    home_page.open_global_feed_tab()
    likes_before_click = home_page.get_number_of_last_article_likes()
    home_page.click_on_heart_icon_on_last_article()
    article_title = home_page.get_last_article_title()
    profile_page.open_profile_page()
    profile_page.open_favourite_tab()
    assert home_page.get_number_of_last_article_likes() == likes_before_click + 1
    assert article_title == profile_page.get_first_article_title()
    profile_page.click_on_heart_icon()


def test_unmark_article_as_favourite(init_driver, login_user):
    home_page = HomePage(init_driver)
    profile_page = ProfilePage(init_driver)
    home_page.open_global_feed_tab()
    likes_before_click = home_page.get_number_of_last_article_likes()
    home_page.click_on_heart_icon_on_last_article()
    article_title = home_page.get_last_article_title()
    profile_page.open_profile_page()
    profile_page.open_favourite_tab()
    assert home_page.get_number_of_last_article_likes() == likes_before_click + 1
    assert article_title == profile_page.get_first_article_title()
    home_page.open_home_page()
    home_page.open_global_feed_tab()
    home_page.click_on_heart_icon_on_last_article()
    home_page.wait_until_class_changes(home_page.MARKED_HEART)
    assert home_page.get_number_of_last_article_likes() == likes_before_click


def test_mark_multiple_article_as_favourite(init_driver, login_user):
    home_page = HomePage(init_driver)
    home_page.open_global_feed_tab()
    likes_before_click1 = home_page.get_number_of_second_last_article_likes()
    likes_before_click2 = home_page.get_number_of_last_article_likes()
    home_page.click_on_heart_icon_on_last_article()
    home_page.click_on_heart_icon_on_second_last_article()
    home_page.wait_until_class_changes(home_page.UNMARKED_HEART)
    assert home_page.get_number_of_second_last_article_likes() == likes_before_click1 + 1
    assert home_page.get_number_of_last_article_likes() == likes_before_click2 + 1
    home_page.click_on_heart_icon_on_last_article()
    home_page.click_on_heart_icon_on_second_last_article()
