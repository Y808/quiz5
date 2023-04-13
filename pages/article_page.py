from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ArticlePage(BasePage):
    ARTICLE_TITLE = (By.XPATH, "//h1")

    def get_title_text(self):
        print(self.get_text(self.ARTICLE_TITLE))
        return self.get_text(self.ARTICLE_TITLE)
