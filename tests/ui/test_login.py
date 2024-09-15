import pytest
from time import sleep
from pages.auth.login_page import LoginPage
from dotenv import load_dotenv
# from utils.common import read_excel
import os
@pytest.mark.usefixtures("init_driver")
class TestLogin:
    BASE_URL="https://www.saucedemo.com"
    def setup_method(self):
        """Setup before each test method"""
        self.driver.get(self.BASE_URL)
        self.page = LoginPage(self.driver)
    @pytest.mark.parametrize(
        "username, password",
        [("standard_user", "secret_sauce"),
         ]
            # read_excel(os.path.join("datafiles/auth", "valid_login.xlsx"))

    )
    
    def test_login_valid(self, username, password):
        """Test login with various scenarios"""
        self.page.action_login(username, password)
        sleep(3)
        assert self.page.utils.is_on_page("inventory")
