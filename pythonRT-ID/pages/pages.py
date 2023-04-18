
from selenium.webdriver.common.by import By
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
        self.lnk_reg = driver.find_element(*AuthLocators.LNK_REG)

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

    def click_lnk_reg(self):
        # Клик по ссылке "Зарегистрироваться"
        self.lnk_reg.click()


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
        url = "https://mail.ru"
        self.driver.execute_script(f"window.open('{url}','_blank');")
        driver.switch_to.window(driver.window_handles[1])
        self.email_page = driver.find_element(*AuthLocators.EMAIL_PAGE)

        time.sleep(3)

    def enter_email_page(self):
        # Клик по кнопке "Почта"
        self.email_page.click()

    def input_email_username(self, value):
        # Ввод логина от почтового ящика
        self.driver.find_element(By.NAME, "username").send_keys(value)

    def save_username(self):
        # Отключение чек-бокса "Запомнить меня"
        self.driver.find_element(By.CLASS_NAME, "save-auth-field-wrap").click()

    def click_to_input_pass(self):
        # Клик по кнопке "Ввести пароль"
        self.driver.find_element(By.CLASS_NAME, "submit-button-wrap").click()

    def input_email_password(self, value):
        # Ввод пароля от почтового ящика
        self.driver.find_element(By.NAME, "password").send_keys(value)

    def click_to_enter_inbox_email(self):
        # Клик по кнопке "Войти"
        self.driver.find_element(By.CLASS_NAME, "submit-button-wrap").click()

    def first_mail_by_word(self, value):
        # Выбор крайнего письма по содержанию комбинации слов
        self.driver.find_element(By.PARTIAL_LINK_TEXT, value).click()

    def get_first_mail_text(self):
        # Получение текста письма
        return self.driver.find_element(By.CLASS_NAME, "letter-body__body-content").text
