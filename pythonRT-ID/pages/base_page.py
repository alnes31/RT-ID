from urllib.parse import urlparse
from selenium.webdriver.common.by import By


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
        user_lastname = self.driver.find_element(By.CLASS_NAME, "user-name__last-name")
        return user_lastname.text

    def get_error_message(self):
        err_message = self.driver.find_element(By.ID, "form-error-message")
        return err_message.text

    def get_username_placeholder(self):
        username_placeholder = self.driver.find_element(By.CLASS_NAME, "rt-input__placeholder")
        return username_placeholder.text

    def get_title_input_code(self):
        title_input_code = self.driver.find_element(By.CLASS_NAME, "card-container__title")
        return title_input_code.text


