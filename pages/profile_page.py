import configs
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    MY_ARTICLES_TAB = (By.XPATH, "//a[contains(text(),'My')]")
    FAVOURITE_TAB = (By.XPATH, "//a[contains(text(),'Favor')]")
    FIRST_ARTICLE_TITLE = (By.XPATH, "//h1")
    PROFILE_URL = configs.base_url + '#/@Anna%20MARIA?_k=dhqs1m'

    def open_profile_page(self):
        self.driver.get(self.PROFILE_URL)
        self.wait_until_page_is_loaded()

    def get_first_article_title(self):
        print(self.get_text(self.FIRST_ARTICLE_TITLE))
        return self.get_text(self.FIRST_ARTICLE_TITLE)

    def open_favourite_tab(self):
        self.click(self.FAVOURITE_TAB)
        self.wait_until_page_is_loaded()
