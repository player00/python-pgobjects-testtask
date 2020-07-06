from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MyAccountLocators:
    LOCATOR_USER_INFO_SPAN = (By.CSS_SELECTOR, ".account span")
    LOCATOR_PAGE_TITLE = (By.CLASS_NAME, "page-heading")

class MyAccountHelper(BasePage):


    def get_user_info(self):
        return self.find_element(MyAccountLocators.LOCATOR_USER_INFO_SPAN, time=2).text


    def get_page_title(self):
        return self.find_element(MyAccountLocators.LOCATOR_PAGE_TITLE, time=2).text
        