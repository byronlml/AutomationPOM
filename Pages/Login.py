from Locators.Login import LocatorLogin
from Helper.SeleniumMethods import WebDriverFunctions
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.loc_login = LocatorLogin()
        self.helper = WebDriverFunctions(self.driver)

    def username(self, username):
        user = self.driver.find_element(By.ID, self.loc_login.username_id)
        user.clear()
        user.send_keys(username)

    def password(self, password):
        user = self.driver.find_element(By.ID, self.loc_login.password_id)
        user.clear()
        user.send_keys(password)

    def login_button(self):
        user = self.driver.find_element(By.ID, self.loc_login.login_button_id)
        user.click()

    def logged_user(self):
        return self.driver.find_element(By.XPATH, self.loc_login.logged_user_xpath).text
