
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import configs


class NewArticlePage(BasePage):
    ARTICLE_TITLE = (By.XPATH, "//input[@placeholder='Article Title']")
    DESCRIPTION_SECTION = (By.XPATH, "//fieldset[@class='form-group'][2]/input")
    ARTICLE_SECTION = (By.XPATH, "//textarea")
    TAGS = (By.XPATH, "//input[@placeholder='Enter tags']")
    SUBMIT_BUTTON = (By.XPATH, "//button")
    TITLE_ERROR = (By.XPATH, "//li[contains(text(),'title')]")
    DESCRIPTION_ERROR = (By.XPATH, "//li[contains(text(),'description')]")
    BODY_ERROR = (By.XPATH, "//li[contains(text(),'body')]")
    NEW_ARTICLE_URL = configs.base_url + "#/editor?_k=ai5mbs"

    def open_new_article_page(self):
        self.driver.get(self.NEW_ARTICLE_URL)

    def create_new_article(self, title=None, about=None, body=None, tags=None):
        if title:
            self.fill_input(self.ARTICLE_TITLE, title)
        if about:
            self.fill_input(self.DESCRIPTION_SECTION, about)
        if body:
            self.fill_input(self.ARTICLE_SECTION, body)
        if tags:
            self.fill_input(self.TAGS, tags)
        self.click(self.SUBMIT_BUTTON)

    def get_title_error_text(self):
        print(self.get_text(self.TITLE_ERROR))
        return self.get_text(self.TITLE_ERROR)

    def get_about_error_text(self):
        print(self.get_text(self.DESCRIPTION_ERROR))
        return self.get_text(self.DESCRIPTION_ERROR)

    def get_body_error_text(self):
        print(self.get_text(self.BODY_ERROR))
        return self.get_text(self.BODY_ERROR)
