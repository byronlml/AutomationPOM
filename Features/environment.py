from selenium import webdriver


def before_scenario(self, scenario):
    print("before is working")
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()


def after_scenario(self, scenario):
    print("after is working")
    self.driver.close()


