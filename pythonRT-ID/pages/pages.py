from .base_page import BasePage
from .locators import AuthLocators

import time
import os


class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        # *** Инициализируем локаторы для страницы авторизации

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
        # Ввод данных авторизации (телефон, почта, логин, ЛС)
        self.username.send_keys(value)

    def enter_pass(self, value):
        # Ввод пароля на странице авторизации
        self.psswrd.send_keys(value)

    def btn_auth_click(self):
        # Нажатие кнопки авторизации
        self.btn_auth.click()

    def btn_phone_click(self):
        # Выбор таба "Телефон"
        self.btn_phone.click()

    def btn_email_click(self):
        # Выбор таба "Почта"
        self.btn_email.click()

    def btn_login_click(self):
        # Выбор таба "Логин"
        self.btn_login.click()

    def btn_ls_click(self):
        # Выбор таба "Лицевой счёт"
        self.btn_ls.click()


class AuthCodePage(BasePage):

    def __init__(self, driver, timeout=10):
        # Инициализируем локаторы для страницы авторизации

        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://lk.rt.ru"
        driver.get(url)
        self.input_adr = driver.find_element(*AuthLocators.IDENT_FOR_CODE)
        self.get_code_btn = driver.find_element(*AuthLocators.GET_CODE_BTN)
        time.sleep(3)

    def btn_get_code_click(self):
        # Клик по кнопке "Получить код"
        self.get_code_btn.click()

    def enter_ident(self, value):
        # Ввод данных идентификации (телефон или почта)
        self.input_adr.send_keys(value)


class EmailPage(BasePage):

    def __init__(self, driver, timeout=10):
        # Инициализируем локаторы для страницы почтового ящика

        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://mail.ru"
        driver.get(url)
        self.email_page = driver.find_element(*AuthLocators.EMAIL_PAGE)
        # self.input_username = driver.find_element(*AuthLocators.EMAIL_USERNAME)
        time.sleep(3)

    def enter_email_page(self):
        # Клик по кнопке "Почта"
        self.email_page.click()

    def input_email_username(self, value):
        self.driver.find_element(*AuthLocators.EMAIL_USERNAME).send_keys(value)




