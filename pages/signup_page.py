from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import configs


class SignupPage(BasePage):
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder = 'Username']")
    EMAIL_FIELD = (By.XPATH, "//input[@placeholder = 'Email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder = 'Password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type = 'submit']")
    USERNAME_ERROR = (By.XPATH, "//li[contains(text(),'username')]")
    EMAIL_ERROR = (By.XPATH, "//li[contains(text(),'email')]")
    PASSWORD_ERROR = (By.XPATH, "//li[contains(text(),'password')]")
    SIGNUP_URL = configs.base_url + "#/register?_k=efbs31"

    def open_signup_page(self):
        self.driver.get(self.SIGNUP_URL)

    def signup(self, username, email, password):
        self.fill_input(self.USERNAME_FIELD, username)
        self.fill_input(self.EMAIL_FIELD, email)
        self.fill_input(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BUTTON)

    def get_taken_username_error_text(self):
        print(self.get_text(self.USERNAME_ERROR))
        return self.get_text(self.USERNAME_ERROR)

    def get_password_error_text(self):
        print(self.get_text(self.PASSWORD_ERROR))
        return self.get_text(self.PASSWORD_ERROR)

    def get_email_error_text(self):
        print(self.get_text(self.EMAIL_ERROR))
        return self.get_text(self.EMAIL_ERROR)
