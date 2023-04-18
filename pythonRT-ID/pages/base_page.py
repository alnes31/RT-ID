from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from .locators import AuthLocators


class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы и время ожидани элементов
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_positive_lastname(self):
        # Получение Значения для фамилии как подтверждение успешной авторизации
        user_lastname = self.driver.find_element(By.CLASS_NAME, "user-name__last-name")
        return user_lastname.text

    def get_error_message(self):
        # Получение текста сообщения об ошибке
        err_message = self.driver.find_element(By.ID, "form-error-message")
        return err_message.text

    def get_username_placeholder(self):
        # Получение значения подписи для поля ввода авторизационных данных
        username_placeholder = self.driver.find_element(By.CLASS_NAME, "rt-input__placeholder")
        return username_placeholder.text

    def get_title_input_code(self):
        # Получение заголовка формы, как подтверждение, что открылась именно форма ввода кода авторизации
        title_input_code = self.driver.find_element(By.CLASS_NAME, "card-container__title")
        return title_input_code.text

    def send_auth_code(self, value):
        # Заполнение полей ввода для кода авторизации
        self.driver.find_element(By.CLASS_NAME, "rt-input__input").send_keys(value)

    def get_title(self):
        # Получение заголовка страницы по имени тега
        return self.driver.find_element(By.TAG_NAME, "title").text

    def input_reg_name(self, value):
        # Заполнение регистрационного имени
        reg_name = self.driver.find_element(*AuthLocators.REG_NAME)
        reg_name.send_keys(value)

    def input_reg_lastname(self, value):
        # Заполнение регистрационной фамилии
        reg_lastname = self.driver.find_element(*AuthLocators.REG_FAM)
        reg_lastname.send_keys(value)

    def input_reg_email(self, value):
        # Заполнение регистрационной почты
        reg_email = self.driver.find_element(*AuthLocators.REG_EMAIL)
        reg_email.send_keys(value)

    def input_reg_pass(self, value):
        # Заполнение регистрационного пароля
        reg_pass = self.driver.find_element(*AuthLocators.REG_PASS)
        reg_pass.send_keys(value)

    def input_reg_pass_confirm(self, value):
        # Заполнение регистрационного пароля (подтверждение)
        reg_pass_confirm = self.driver.find_element(*AuthLocators.REG_PASS_CONFIRM)
        reg_pass_confirm.send_keys(value)

    def click_btn_reg(self):
        # Клик по кнопке "Зарегистрироваться"
        self.driver.find_element(By.CLASS_NAME, "register-form__reg-btn").click()
