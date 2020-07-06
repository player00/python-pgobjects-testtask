from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from users import User


class LoginLocators:
    LOCATOR_EMAIL_FIELD = (By.ID, "email")
    LOCATOR_PASSWORD_FIELD = (By.ID, "passwd")
    LOCATOR_SIGN_IN_BUTTON = (By.ID, "SubmitLogin")


class LoginHelper(BasePage):

    def enter_email(self, email: str):
        email_field = self.find_element(LoginLocators.LOCATOR_EMAIL_FIELD)
        email_field.click()
        email_field.send_keys(email)
        return email_field

    def enter_password(self, password: str):
        password_field = self.find_element(LoginLocators.LOCATOR_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def click_sign_in_button(self):
        return self.find_element(LoginLocators.LOCATOR_SIGN_IN_BUTTON, time=2).click()

    def login(self, user: User):
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.click_sign_in_button()
