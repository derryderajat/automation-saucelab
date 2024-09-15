from pages.auth.login_page import LoginPage
from time import sleep
def perform_login(driver, username, password):
    """Test login with various scenarios"""
    page = LoginPage(driver)
    page.action_login(username, password)
    sleep(3)
    assert page.utils.is_on_page("inventory")