import pytest
from time import sleep
from utils.login_util import perform_login
from pages.products_page import ProductsPage


@pytest.mark.usefixtures("init_driver")
class TestProducts:
    BASE_URL = "https://www.saucedemo.com"

    def setup_method(self):
        """Setup before each test method"""
        self.driver.get(self.BASE_URL)
        perform_login(self.driver,"standard_user","secret_sauce")
        self.page = ProductsPage(self.driver)
    # @pytest.nark.reg

    def test_add_product_to_cart(self):
        self.page.add_item_to_cart("NONE")

