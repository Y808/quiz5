from telnetlib import EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import configs


class LoginPage(BasePage):
    EMAIL_FIELD = (By.XPATH, "//input[@type = 'email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type = 'password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type = 'submit']")
    EMAIL_ERROR = (By.XPATH, "//li[contains(text(),'email')]")
    PASSWORD_ERROR = (By.XPATH, "//li[contains(text(),'password')]")
    LOGIN_URL = configs.base_url + "#/login"


    def open_login_page(self):
        self.driver.get(self.LOGIN_URL)
        self.wait_until_page_is_loaded()

    def login(self, email, password):
        self.fill_input(self.EMAIL_FIELD, email)
        self.fill_input(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        self.wait_until_page_is_loaded()

    def get_email_error_text(self):
        print(self.get_text(self.EMAIL_ERROR))
        return self.get_text(self.EMAIL_ERROR)

    def get_password_error_text(self):
        print(self.get_text(self.PASSWORD_ERROR))
        return self.get_text(self.PASSWORD_ERROR)
