from behave import *
from Helper.SeleniumMethods import WebDriverFunctions
import time
from Pages.Login import LoginPage

url = "https://practicetestautomation.com/practice-test-login/"


@given('User on login page')
def open_url(self):
    WebDriverFunctions(self.driver).open_url(url)
    time.sleep(5)


@when('User enter "{username}" and "{password}"')
def step_impl(self, username, password):
    LoginPage(self.driver).username(username)
    LoginPage(self.driver).password(password)


@when('User click on login button')
def step_impl(self):
    LoginPage(self.driver).login_button()
    time.sleep(1)


@then('Would show the user page')
def step_impl(self):
    text = LoginPage(self.driver).logged_user()
    assert text == "Logged In Successfully"
