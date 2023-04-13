import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def login_user(init_driver, read_login_users):
    login_page = LoginPage(init_driver)
    email = read_login_users["validUser1"]["email"]
    password = read_login_users["validUser1"]["password"]
    login_page.open_login_page()
    login_page.login(email, password)
    yield email, password


def test_click_on_tag(init_driver, login_user):
    home_page = HomePage(init_driver)
    home_page.open_global_feed_tab()
    home_page.click_on_popular_tag()
    tag_name = home_page.get_tag_name()
    nav_link_name = home_page.get_nav_name()
    assert tag_name == nav_link_name
    assert home_page.all_articles_have_tag("implementations"), "There is an article with different tag rather than 'implementations'"



