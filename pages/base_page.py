from datetime import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configs


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = configs.base_url
        self.wait = WebDriverWait(self.driver, configs.default_wait_time)

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def fill_input(self, locator, text):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.clear()
        el.send_keys(text)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_title(self):
        return self.driver.title

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def get_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def wait_until_page_is_loaded(self):
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def get_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_until_class_changes(self, locator, class_name):

        element = self.wait.until(EC.presence_of_element_located(locator))
        current_classes = element.get_attribute('class').split()
        if class_name not in current_classes:
            self.wait.until(EC.element_attribute_to_be(locator, 'class', f'* {class_name} *'))
