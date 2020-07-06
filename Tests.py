from pages.MyStorePage import MyStoreHelper
from pages.LoginPage import LoginHelper
from pages.MyAccountPage import MyAccountHelper
from pages.LoginPage import LoginUsers

def test_login(browser):
    my_store_page = MyStoreHelper(browser)
    my_store_page.go_to_site()
    my_store_page.click_sign_in_button()
    login_page = LoginHelper(browser)
    login_page.enter_email(LoginUsers.USER_1['email'])
    login_page.enter_password(LoginUsers.USER_1['password'])
    login_page.click_sign_in_button()
    my_account_page = MyAccountHelper(browser)
    assert my_account_page.get_user_info() == "Selenuim IsGood"

