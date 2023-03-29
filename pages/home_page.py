from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    WORKSPACE_NAME = (By.XPATH, "//li[@class='nav-item'][4]/a")
    YOUR_FEED_TAB = (By.XPATH, "//a[contains(text(),'Your Feed')]")
    GLOBAL_FEED_TAB = (By.XPATH, "//a[contains(text(),'Global Feed')]")
    LIKES_NUMBER_ON_LAST_ARTICLE = (By.XPATH, "(//button[@class='btn btn-sm btn-outline-primary'])[last()]")
    FAVOURITE_BTN_ON_LAST_ARTICLE = (By.XPATH, "(//div[@class='pull-xs-right'])[last()]")
    FAVOURITE_BTN_ON_SECOND_LAST_ARTICLE = (By.XPATH, "(//div[@class='pull-xs-right'])[last()-1]")
    LAST_ARTICLE_TITLE = (By.XPATH, "(//a[@class='preview-link']/h1)[last()]")

    def get_workspace_text(self):
        print(self.get_text(self.WORKSPACE_NAME))
        return self.get_text(self.WORKSPACE_NAME)

    def get_your_feed_tab(self):
        return self.get_element(self.YOUR_FEED_TAB)

    def open_global_feed_tab(self):
        self.wait_until_page_is_loaded()
        self.click(self.GLOBAL_FEED_TAB)

    def get_number_of_last_article_likes(self):
        print(self.get_text(self.FAVOURITE_BTN_ON_LAST_ARTICLE))
        return int(self.get_text(self.FAVOURITE_BTN_ON_LAST_ARTICLE))

    def get_number_of_second_last_article_likes(self):
        print(self.get_text(self.FAVOURITE_BTN_ON_SECOND_LAST_ARTICLE))
        return int(self.get_text(self.FAVOURITE_BTN_ON_SECOND_LAST_ARTICLE))

    def get_last_article_title(self):
        print(self.get_text(self.LAST_ARTICLE_TITLE))
        return self.get_text(self.LAST_ARTICLE_TITLE)

    def click_on_heard_icon_on_last_article(self):
        self.scroll_to_element(self.FAVOURITE_BTN_ON_LAST_ARTICLE)
        self.click(self.FAVOURITE_BTN_ON_LAST_ARTICLE)
        # self.wait_until_class_changes(self.LIKES_NUMBER_ON_LAST_ARTICLE, 'btn btn-sm btn-primary')

    def click_on_heard_icon_on_second_last_article(self):
        self.scroll_to_element(self.FAVOURITE_BTN_ON_SECOND_LAST_ARTICLE)
        self.click(self.FAVOURITE_BTN_ON_SECOND_LAST_ARTICLE)
