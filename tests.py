from pages.mystorepage import MyStoreHelper
from pages.loginpage import LoginHelper
from pages.myaccountpage import MyAccountHelper
from users import *

def test_login(browser):
    my_store_page = MyStoreHelper(browser)
    my_store_page.go_to_site()
    my_store_page.click_sign_in_button()
    login_page = LoginHelper(browser)
    login_page.login(VALID_USER_1)
    my_account_page = MyAccountHelper(browser)
    assert my_account_page.get_user_info() == "Selenuim IsGood"

