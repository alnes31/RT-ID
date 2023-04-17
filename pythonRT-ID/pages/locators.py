from selenium.webdriver.common.by import By

class AuthLocators:
    AUTH_USERNAME = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.CLASS_NAME, "login-form__login-btn")
    PHONE_BTN = (By.ID, "t-btn-tab-phone")
    EMAIL_BTN = (By.ID, "t-btn-tab-mail")
    LOGIN_BTN = (By.ID, "t-btn-tab-login")
    LS_BTN = (By.ID, "t-btn-tab-ls")

class LKLocators:
    USER_LASTNAME = (By.CLASS_NAME, "user-name__last-name")
