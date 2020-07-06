from pages.my_store import MyStoreHelper
from pages.login import LoginHelper
from pages.my_account import MyAccountHelper
from users import VALID_USER_1

def test_successful_login(browser):
    my_store_page = MyStoreHelper(browser)
    my_store_page.go_to_site()
    my_store_page.click_sign_in_button()
    login_page = LoginHelper(browser)
    login_page.login(VALID_USER_1)
    my_account_page = MyAccountHelper(browser)
    assert my_account_page.get_user_info() == "Selenuim IsGood"

