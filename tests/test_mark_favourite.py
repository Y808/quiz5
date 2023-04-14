import pytest

from pages.home_page import HomePage
from pages.profile_page import ProfilePage


@pytest.fixture
def unmark_the_favourite(init_driver):
    yield
    profile_page = ProfilePage(init_driver)
    profile_page.open_profile_page()
    profile_page.open_favourite_tab()
    while profile_page.is_heart_icon_present():
        profile_page.click_on_heart_icon()
        profile_page.reload_page()


def test_mark_article_as_favourite(init_driver, main_user_login, unmark_the_favourite):
    home_page = HomePage(init_driver)
    profile_page = ProfilePage(init_driver)
    home_page.open_global_feed_tab()
    likes_before_click = home_page.get_number_of_last_article_likes()
    home_page.click_on_heart_icon_on_last_article()
    article_title = home_page.get_last_article_title()
    profile_page.open_profile_page()
    profile_page.open_favourite_tab()
    assert home_page.get_number_of_last_article_likes() == likes_before_click + 1, "likes after click != likes_before_click + 1"
    assert article_title == profile_page.get_first_article_title(), "article title of liked article not match on 'favoutrite articles' tab"



def test_unmark_article_as_favourite(init_driver, main_user_login):
    home_page = HomePage(init_driver)
    profile_page = ProfilePage(init_driver)
    home_page.open_global_feed_tab()
    likes_before_click = home_page.get_number_of_last_article_likes()
    home_page.click_on_heart_icon_on_last_article()
    article_title = home_page.get_last_article_title()
    profile_page.open_profile_page()
    profile_page.open_favourite_tab()
    assert home_page.get_number_of_last_article_likes() == likes_before_click + 1, "likes after click != likes_before_click + 1"
    assert article_title == profile_page.get_first_article_title(), "article title of liked article not match on 'favoutrite articles' tab"
    home_page.open_home_page()
    home_page.open_global_feed_tab()
    home_page.click_on_heart_icon_on_last_article()
    home_page.wait_until_class_changes(home_page.MARKED_HEART)
    assert home_page.get_number_of_last_article_likes() == likes_before_click


def test_mark_multiple_article_as_favourite(init_driver, main_user_login, unmark_the_favourite):
    home_page = HomePage(init_driver)
    profile_page = ProfilePage(init_driver)
    home_page.open_global_feed_tab()
    likes_before_click1 = home_page.get_number_of_second_last_article_likes()
    likes_before_click2 = home_page.get_number_of_last_article_likes()
    home_page.click_on_heart_icon_on_last_article()
    home_page.click_on_heart_icon_on_second_last_article()
    home_page.wait_until_class_changes(home_page.UNMARKED_HEART)
    assert home_page.get_number_of_second_last_article_likes() == likes_before_click1 + 1, "likes after click != likes_before_click + 1"
    assert home_page.get_number_of_last_article_likes() == likes_before_click2 + 1, "likes after click != likes_before_click + 1"
"""    profile_page.open_profile_page()
    profile_page.open_favourite_tab()
    profile_page.click_on_heart_icon()
    profile_page.reload_page()
    profile_page.click_on_heart_icon()"""
