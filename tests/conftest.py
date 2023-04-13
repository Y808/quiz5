import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeType
from tests.data.login_users import user1Email, user1Password
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture
def init_driver(request):
    browser_name = request.config.getoption("--browser")
    global driver, driver_options
    if browser_name in "chrome":
        driver_options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=driver_options)
    elif browser_name == "firefox":
        driver_options = webdriver.FirefoxOptions()
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=driver_options)
    elif browser_name == "chrome_headless":
        driver_options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        driver = webdriver.Chrome(service=service, options=driver_options)
        driver_options.add_argument("--no-sandbox")
        driver_options.add_argument("--headless")
        driver_options.add_argument("--disable-dev-shm-usage")
        # driver_options.add_argument('--disable-gpu')
        # driver_options.add_argument('disable-infobars')
        # driver_options.add_argument("--disable-extensions")

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
    # driver.close()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser: chrome, firefox or chrome headless"
    )


@pytest.fixture
def read_login_users():
    return {"user1Email": user1Email, "user1Password": user1Password}


@pytest.fixture
def main_user_login(init_driver):
    login_page = LoginPage(init_driver)
    email = user1Email
    password = user1Password
    login_page.open_login_page()
    login_page.login(email, password)
    home_page = HomePage(init_driver)
    home_page.wait_until_page_is_loaded()
    yield email, password
