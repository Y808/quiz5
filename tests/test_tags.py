from pages.home_page import HomePage


def test_click_on_tag(init_driver, main_user_login):
    home_page = HomePage(init_driver)
    home_page.open_global_feed_tab()
    home_page.click_on_popular_tag()
    tag_name = home_page.get_tag_name()
    nav_link_name = home_page.get_nav_name()
    assert tag_name == nav_link_name, "Tag name is not the same as navigation tab"
    assert home_page.all_articles_have_tag(
        "implementations"), "There is an article with different tag rather than 'implementations'"
