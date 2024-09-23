from selenium.webdriver.common.by import By

class ProductsLocators:
    TITLE_TEXT = (By.XPATH, "//*[@data-test='title']")
    INVENTORY_LIST = (By.XPATH, "//*[@data-test='inventory-list']")
    INVENTORY_ITEM_NAME = (By.XPATH, "//*[@data-test='inventory_item_name']")
    INVENTORY_ITEM_DESC = (By.XPATH, "//*[@data-test='inventory_item_desc']")
    INVENTORY_ITEM_PRICE = (By.XPATH, "//*[@data-test='inventory-item-price']")
    ADD_CART_BUTTON = (By.XPATH, "//div[contains(@class, 'pricebar')]/button")