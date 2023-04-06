from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import configs


class SettingsPage(BasePage):
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Username']")
    BIO_FIELD = (By.XPATH, "//textarea")
    EMAIL_FIELD = (By.XPATH, "//input[@type = 'email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type = 'password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type = 'submit']")
    SETTINGS_URL = configs.base_url + "#/settings"

    def open_settings_page(self):
        self.driver.get(self.SETTINGS_URL)

    def change_password_and_bio(self, password, bio):
        self.fill_input(self.PASSWORD_FIELD, password)
        self.fill_input(self.BIO_FIELD, bio)
        self.click(self.SUBMIT_BUTTON)

