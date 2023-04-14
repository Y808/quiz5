import pytest
import requests
from helpers.utils import generate_random_credentials
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture
def new_user():
    random_cred = generate_random_credentials()
    email = random_cred["email"]
    username = random_cred["username"]
    password = random_cred["email"]
    user = {
        "user": {
            "email": email,
            "username": username,
            "password": password
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post("https://api.realworld.io/api/users", json=user, headers=headers)

    assert response.status_code == 200, f"Failed to sign up user with API. Response code: {response.status_code}. Response text: {response.text}"
    print(response.text)
    print(response.status_code)
    yield random_cred

def test_login_with_api(init_driver, new_user):

    login_page = LoginPage(init_driver)
    home_page = HomePage(init_driver)
    login_page.open_login_page()
    login_page.login(new_user['email'], new_user['password'])
    home_page.wait_until_page_is_loaded()

    assert new_user['username'] == home_page.get_workspace_text(), "username on signup is not the same as on workspace"
    assert home_page.get_your_feed_tab().is_enabled(), "YOUR_FEED_TAB is not enabled"
