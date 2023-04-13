import configs
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    MY_ARTICLES_TAB = (By.XPATH, "//a[contains(text(),'My')]")
    FAVOURITE_TAB = (By.XPATH, "//a[contains(text(),'Favor')]")
    FIRST_ARTICLE_TITLE = (By.XPATH, "//h1")
    HEART_ICON = (By.CSS_SELECTOR, "div.pull-xs-right")
    MARKED_HEART = (By.XPATH, "//button[@class= 'btn btn-sm btn-primary']")
    PROFILE_URL = configs.base_url + '#/@Anna%20MARIA?_k=r5761m'

    def open_profile_page(self):
        self.driver.get(self.PROFILE_URL)
        self.wait_until_page_is_loaded()
        self.find_element(self.FAVOURITE_TAB)

    def get_first_article_title(self):
        print(self.get_text(self.FIRST_ARTICLE_TITLE))
        return self.get_text(self.FIRST_ARTICLE_TITLE)

    def open_favourite_tab(self):
        self.click(self.FAVOURITE_TAB)
        self.find_element(self.FAVOURITE_TAB)
        self.wait_until_page_is_loaded()

    def click_on_hearts_icon(self, heart_icons):
        self.find_element(self.HEART_ICON)
        print(f"Number of heart icons: {len(heart_icons)}")  # print length of heart_icons list
        for heart_icon in heart_icons:
            try:
                heart_icon.click()
            except:
                print("Error clicking on heart icon")

    def click_on_heart_icon(self):
        self.click(self.HEART_ICON)
        self.wait_until_class_changes(self.MARKED_HEART)
        self.wait_until_page_is_loaded()
