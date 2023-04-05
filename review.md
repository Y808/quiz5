#### 1. Create your path in a way working in all systems (mac/linux/windows)
```python
from pathlib import Path
import os

def read_login_users(): 
    with open(str(Path(os.path.abspath(__file__)).parent) + "/data/loginUsers.json") as f:
        login_users = json.load(f)
    return login_users
```
#### 2. Do not use `place holders` for locators if you don't have to. Use id, type, class, name instead. In general try to not write your locators based the text. 

```python
"//input[@placeholder = 'Username']" # it is ok because we don't have any specific attribute related to Username field in signup
"//input[@placeholder = 'Email']" # the better locator is "//input[@type = 'Email']" because placeholder text might be change in the future
```
> Your task: I changed the Signup page locators. Do the same for other pages

#### 3. Do not include header values in urls until you should. 
signup_page.py
```python
SIGNUP_URL = configs.base_url + "#/register?_k=efbs31" # "#/register" is ok.
```
> Your task: Signup page changed, do the same for other pages as well. 

#### 4. Keep your code as simple as you can. There is no need to use XML parsing for comparing a text of the element with a string. In your signup tests, instead of `strings.xml` you can have a simple python or json file to keep your strings, and then just simply compare and assert. I have removed `strings.xml` and `read_strings_xml` in conftest. 

strings.py
```python
taken_username = "username has already been taken"
blank_username = "username can't be blank"
```
> Your task (1): Change tests and fix errors in all tests files to use this brand-new implementation. I did for signup.

> Your task (2): Create a simple python file for keeping `login_users` (takenUsername, validUser1), instead of `loginUsers.json` and use them for assertions. This way the json file hasn't to be read each time and the final code will be much simpler.At the end delete unused files, imports, functions.

> Your task (3): We have some rules called Python Zen which are really good to read. Open a new python file and then just write `import this`, run it and read python Zen!
#### 5. Keep your code clean
- Remove any unused Imports/ Functions / Files / Comments. (Don't worry as long as your project is tracked with git you can retriew back ans see the history for almost everything)
- Keep code formatted according to PEP, you can press CTRL+ALT+L in Pycharm
- Remove unused empty lines (Usually between imports).

> Your task (at the end of all tasks): Look through all the files and clean them

#### 6. Make your tests deliverable
To test successful signup functionality, we need unique username each time to test it. So the solution is creating a random username, but this is not possible using JSON file. We should have a python module and define a function (keyword) to generate unique username. 
1. Added a keyword called `generate_random_string` in`helpers/utils.py` to achieve this. This function accepts prefix, length and option to use special characters.
2. Changed the `test_successful_signup` by using this keyword. 

- ***Note:*** In a real project you should consider deleting created user from the database in `Teardown` stage. Also you can create a unique user in `Setup` stage for login tests (Since your tests might run in multiple CI machines). 
> Your task (Optional): Add a new test and instead of login with the same user, signup a user with API and then test login functionality with UI.

#### 7. Each function (keyword) should have 1 responsibility. The same for the tests.
> Your task: separate `settings_page.py/change_password_and_bio` to two different functions and then separate the related test (test_change_password_and_bio) to two different test.

#### 8. Keep in your mind you should never use `time.sleep()` until there is no way. 
> Your task: Search the entire project for `time.sleep()` and try replace them with Expected Conditions. (like in `test_settings.py`)

#### 9. You should always have assertions checking what you have done in your tests. 
> Your task (1): In `test_settings.py/test_change_password_and_bio` which should be two tests now (according to item 6), add assertions to check whether the bio and password are changed.  
> Your task (2): In `test_navigate_to_pages.py` write assertions for check something related to that redirected page after `forward` or `back`
> 
#### 10. If you're going to use same user for test functionalities, you should perfectly handle changes happened during the test in `teardown`, so next time you should be able to run the same test again. 
> Your task: `test_mark_favourite` tests are failing. There you can not run the tests multiple times since the status of favourite articles saves in DB. try to change the liked article to unliked after the test.

#### 11. Always try to write assertion message. It will help you a lot when facing an error. Look at `test_tags.py`, I have added one. 
> Your task: Try to add assertion messages for any assertion statement you have in your tests

#### 12. You should copy the same pieces of code in multiple places like `login_user` in almost all tests. This is a principal of clean code called DRY (Do not repeat yourself).
> Your task: Add another login function for main user and use that in tests. You can handle it with `conftest` as well. 

