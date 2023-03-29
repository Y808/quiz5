from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    WORKSPACE_NAME = (By.XPATH, "//li[@class='nav-item'][4]/a")
    SETTINGS_NAV_ITEM = (By.XPATH, "//a[contains(text(),'Settings')]")
    YOUR_FEED_TAB = (By.XPATH, "//a[contains(text(),'Your Feed')]")
    GLOBAL_FEED_TAB = (By.XPATH, "//a[contains(text(),'Global Feed')]")
    POPULAR_TAG = (By.XPATH, "//a[contains(text(),'implementations')]")
    TAG_NAV_LINK = (By.XPATH, "//a[@class='nav-link active']")
    LIKES_NUMBER_ON_LAST_ARTICLE = (By.XPATH, "(//button[@class='btn btn-sm btn-outline-primary'])[last()]")
    FAVOURITE_BTN_ON_LAST_ARTICLE = (By.XPATH, "(//div[@class='pull-xs-right'])[last()]")
    FAVOURITE_BTN_ON_SECOND_LAST_ARTICLE = (By.XPATH, "(//div[@class='pull-xs-right'])[last()-1]")
    ARTICLES_ELEMENT = (By.CLASS_NAME, "article-preview")
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

    def click_on_heart_icon_on_last_article(self):
        self.scroll_to_element(self.FAVOURITE_BTN_ON_LAST_ARTICLE)
        self.click(self.FAVOURITE_BTN_ON_LAST_ARTICLE)
        # self.wait_until_class_changes(self.LIKES_NUMBER_ON_LAST_ARTICLE, 'btn btn-sm btn-primary')

    def click_on_heart_icon_on_second_last_article(self):
        self.scroll_to_element(self.FAVOURITE_BTN_ON_SECOND_LAST_ARTICLE)
        self.click(self.FAVOURITE_BTN_ON_SECOND_LAST_ARTICLE)

    def open_settings_page(self):
        self.wait_until_page_is_loaded()
        self.click(self.SETTINGS_NAV_ITEM)

    def click_on_popular_tag(self):
        self.click(self.POPULAR_TAG)

    def get_tag_name(self):
        print(self.get_text(self.POPULAR_TAG))
        return self.get_text(self.POPULAR_TAG)

    def get_nav_name(self):
        print(self.get_text(self.TAG_NAV_LINK))
        return self.get_text(self.TAG_NAV_LINK)

    def all_articles_have_tag(self, tag_name):
        articles = self.get_elements(self.ARTICLES_ELEMENT)
        for article in articles:
            tags = article.find_elements(By.CLASS_NAME, "tag-list")
            tag_names = [t.text for t in tags[0].find_elements(By.TAG_NAME, "li")]
            if tag_name not in tag_names:
                return False
        return True


