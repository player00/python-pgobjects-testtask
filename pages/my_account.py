from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MyAccountLocators:
    LOCATOR_USER_INFO_SPAN = (By.CSS_SELECTOR, ".account span")

class MyAccountHelper(BasePage):

    def get_user_info(self):
        return self.find_element(MyAccountLocators.LOCATOR_USER_INFO_SPAN, time=2).text