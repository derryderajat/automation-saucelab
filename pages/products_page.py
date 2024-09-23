from locators.products_locators import ProductsLocators as PL
from utils.ui_utils import UIUtils
from time import sleep


class ProductsPage:
    def __init__(self, driver) -> None:
        self.utils = UIUtils(driver)

    def add_item_to_cart(self, item):
        inventory_list = self.utils.find_elements(PL.INVENTORY_LIST)

        print(f"INVENOTRY LIST: {inventory_list}")
        print(f"LENGTH LISTS :{len(inventory_list)}")
