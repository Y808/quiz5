import datetime
from pages.article_page import ArticlePage
from pages.create_article_page import NewArticlePage
from tests.data import strings


def test_publish_blank_title_article(init_driver, main_user_login):
    new_article_page = NewArticlePage(init_driver)
    new_article_page.open_new_article_page()
    new_article_page.wait_until_page_is_loaded()

    title = ""
    about = "This is a test article about section."
    body = "This is a test article body."
    tags = ""

    new_article_page.create_new_article(title, about, body, tags)
    assert new_article_page.get_title_error_text() == strings.blank_article_title, "not blank article error"


def test_publish_blank_about_article(init_driver, main_user_login):
    new_article_page = NewArticlePage(init_driver)
    new_article_page.open_new_article_page()

    title = "Test Article Title"
    about = ""
    body = "This is a test article body."

    new_article_page.create_new_article(title, about, body)
    assert new_article_page.get_about_error_text() == strings.blank_article_description, "not blank description error"


def test_publish_article_with_empty_body(init_driver, main_user_login):
    new_article_page = NewArticlePage(init_driver)
    new_article_page.open_new_article_page()

    title = "Test Article Title"
    about = "This is a test article about section."
    body = ""

    new_article_page.create_new_article(title, about, body)
    assert new_article_page.get_body_error_text() == strings.blank_article_body, "not empty body error"


def test_publish_article(init_driver, main_user_login):
    new_article_page = NewArticlePage(init_driver)
    article_page = ArticlePage(init_driver)
    new_article_page.open_new_article_page()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = f"Test Article Title {timestamp}"
    about = "This is a test article about section."
    body = "This is a test article body."

    new_article_page.create_new_article(title, about, body)
    assert article_page.get_title_text() == title, "title of new created article not match to the opened one"
