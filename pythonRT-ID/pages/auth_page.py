from .base_page import BasePage
from .locators import AuthLocators

import time, os

class AuthPage(BasePage):

    def __init__(self, driver,timeout=10):
        #*** Инициализируем локаторы для страницы авторизации

        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru"
        driver.get(url)
        self.username = driver.find_element(*AuthLocators.AUTH_USERNAME)
        self.psswrd = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn_auth = driver.find_element(*AuthLocators.AUTH_BTN)
        self.btn_phone = driver.find_element(*AuthLocators.PHONE_BTN)
        self.btn_email = driver.find_element(*AuthLocators.EMAIL_BTN)
        self.btn_login = driver.find_element(*AuthLocators.LOGIN_BTN)
        self.btn_ls = driver.find_element(*AuthLocators.LS_BTN)
        time.sleep(3)

    def enter_username(self, value):
        # *** Ввод данных авторизации (телефон, почта, логин, ЛС)
        self.username.send_keys(value)

    def enter_pass(self, value):
        # *** Ввод пароля на странице авторизации
        self.psswrd.send_keys(value)

    def btn_auth_click(self):
        # *** Нажатие кнопки авторизации
        self.btn_auth.click()

    def btn_phone_click(self):
        # *** Выбор таба "Телефон"
        self.btn_phone.click()

    def btn_email_click(self):
        # *** Выбор таба "Почта"
        self.btn_email.click()

    def btn_login_click(self):
        # *** Выбор таба "Логин"
        self.btn_login.click()

    def btn_ls_click(self):
        # *** Выбор таба "Лицевой счёт"
        self.btn_ls.click()


