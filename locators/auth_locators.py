from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_TXT_BOX = (By.ID, "user-name")
    PASSWORD_TXT_BOX = (By.ID,"password")
    LOGIN_BTN = (By.ID, "login-button")