from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import configs
from pages.home_page import HomePage


class SettingsPage(BasePage):
    HEADER = (By.XPATH, "//h1")
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Username']")
    BIO_FIELD = (By.XPATH, "//textarea")
    EMAIL_FIELD = (By.XPATH, "//input[@type = 'email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type = 'password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type = 'submit']")
    LOGOUT_BUTTON = (By.XPATH, "//button[@class='btn btn-outline-danger']")
    SETTINGS_URL = configs.base_url + "#/settings"

    def open_settings_page(self):
        self.driver.get(self.SETTINGS_URL)
        self.find_element(self.SUBMIT_BUTTON)
        self.wait_until_page_is_loaded()

    def change_password(self, password):
        self.fill_input(self.PASSWORD_FIELD, password)
        self.find_element(self.PASSWORD_FIELD)
        self.click(self.SUBMIT_BUTTON)
        self.find_element(HomePage.SETTINGS_NAV_ITEM)
        self.wait_until_page_is_loaded()


    def change_bio(self, bio):
        self.fill_input(self.BIO_FIELD, bio)
        self.scroll_to_element(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)

    def get_bio_text(self):
        print(self.get_text(self.BIO_FIELD))
        return self.get_text(self.BIO_FIELD)

    def get_header_text(self):
        print(self.get_text(self.HEADER))
        return self.get_text(self.HEADER)

    def logout(self):
        self.scroll_to_element(self.LOGOUT_BUTTON)
        self.click(self.LOGOUT_BUTTON)
