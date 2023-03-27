from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    WORKSPACE_NAME = (By.XPATH, "//li[@class='nav-item'][4]/a")

    def get_workspace_text(self):
        print(self.get_text(self.WORKSPACE_NAME))
        return self.get_text(self.WORKSPACE_NAME)


