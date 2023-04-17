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
