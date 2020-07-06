from pages.baseapp import BasePage
from selenium.webdriver.common.by import By

class LoginUsers:
    USER_1 = {
        "email": "seleniumisgood@mail.com",
        "password": "123456"
    }
    
class LoginLocators:
    LOCATOR_EMAIL_FIELD = (By.ID, "email")
    LOCATOR_PASSWORD_FIELD = (By.ID, "passwd")
    LOCATOR_SIGN_IN_BUTTON = (By.ID, "SubmitLogin")

class LoginHelper(BasePage):
    
    def enter_email(self, email):
        email_field = self.find_element(LoginLocators.LOCATOR_EMAIL_FIELD)
        email_field.click()
        email_field.send_keys(email)
        return email_field
    
    def enter_password(self, password):
        password_field = self.find_element(LoginLocators.LOCATOR_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def click_sign_in_button(self):
        return self.find_element(LoginLocators.LOCATOR_SIGN_IN_BUTTON, time=2).click()