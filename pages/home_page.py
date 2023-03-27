from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    WORKSPACE_NAME = (By.XPATH, "//a[@class='nav-link']/img")

    def get_workspace_text(self):
        print(self.get_text(self.WORKSPACE_NAME))
        return self.get_text(self.WORKSPACE_NAME)


