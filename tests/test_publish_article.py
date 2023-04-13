import datetime
import pytest
from pages.article_page import ArticlePage
from pages.create_article_page import NewArticlePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests.data import strings, login_users


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


def test_publish_blank_title_article(init_driver, login_user):
    new_article_page = NewArticlePage(init_driver)
    new_article_page.open_new_article_page()
    new_article_page.wait_until_page_is_loaded()

    title = ""
    about = "This is a test article about section."
    body = "This is a test article body."
    tags = ""

    new_article_page.create_new_article(title, about, body, tags)
    assert new_article_page.get_title_error_text() == strings.blank_article_title


def test_publish_blank_about_article(init_driver, login_user):
    new_article_page = NewArticlePage(init_driver)
    new_article_page.open_new_article_page()

    title = "Test Article Title"
    about = ""
    body = "This is a test article body."

    new_article_page.create_new_article(title, about, body)
    assert new_article_page.get_about_error_text() == strings.blank_article_description


def test_publish_article_with_empty_body(init_driver, login_user):
    new_article_page = NewArticlePage(init_driver)
    new_article_page.open_new_article_page()

    title = "Test Article Title"
    about = "This is a test article about section."
    body = ""

    new_article_page.create_new_article(title, about, body)
    assert new_article_page.get_body_error_text() == strings.blank_article_body


def test_publish_article(init_driver, login_user):
    new_article_page = NewArticlePage(init_driver)
    article_page = ArticlePage(init_driver)
    new_article_page.open_new_article_page()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = f"Test Article Title {timestamp}"
    about = "This is a test article about section."
    body = "This is a test article body."

    new_article_page.create_new_article(title, about, body)
    assert article_page.get_title_text() == title


