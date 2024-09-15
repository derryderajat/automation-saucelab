from utils.ui_utils import UIUtils
from locators.auth_locators import LoginLocators 
from time import sleep
class LoginPage:
    def __init__(self, driver):
        self.utils = UIUtils(driver)
    
    def enter_username(self, username):
        self.utils.send_keys(LoginLocators.USERNAME_TXT_BOX, username)
    
    def enter_password(self, password):
        self.utils.send_keys(LoginLocators.PASSWORD_TXT_BOX, password)
    
    def click_login(self):
        self.utils.click(LoginLocators.LOGIN_BTN)

    def action_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    # def get_error_message(self):
    #     return self.utils.get_text(LoginLocators.ERROR_MESSAGE)

    # def is_dashboard_visible(self):
    #     return self.utils.is_element_visible(LoginLocators.DASHBOARD_TEXT)