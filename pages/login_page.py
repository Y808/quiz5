from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import configs


class LoginPage(BasePage):
    EMAIL_FIELD = (By.XPATH, "//input[@placeholder = 'Email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder = 'Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type = 'submit']")

    def open_login_page(self):
        self.driver.get(self.LOGIN_URL)

    def login(self, email, password):
        self.fill_input(self.EMAIL_FIELD, email)
        self.fill_input(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)


