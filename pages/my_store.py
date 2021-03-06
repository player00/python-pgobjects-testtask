from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MyStoreLocators:
    LOCATOR_SIGN_IN_BUTTON = (By.CLASS_NAME, "login")


class MyStoreHelper(BasePage):

    def click_sign_in_button(self):
        return self.find_element(MyStoreLocators.LOCATOR_SIGN_IN_BUTTON, time=2).click()
