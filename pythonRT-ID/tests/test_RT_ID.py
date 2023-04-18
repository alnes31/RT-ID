import time

from pages.pages import AuthPage
from pages.pages import AuthCodePage
from pages.pages import EmailPage
import datetime
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

LOGIN = os.environ.get("LOGIN")
PSSWRD = os.environ.get("PSSWRD")
PHONE = os.environ.get("PHONE")
EMAIL = os.environ.get("EMAIL")
LS = os.environ.get("LS")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
EMAIL2 = os.environ.get("EMAIL2")
NAME = os.environ.get("NAME")
LASTNAME = os.environ.get("LASTNAME")

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

if os.path.exists('logs'):
    log_file_name = str(f"logs\\log_{datetime.date.today()}-{hour}-{minute}.txt")
else:
    os.mkdir('logs')
    log_file_name = str(f"logs\\log_{datetime.date.today()}-{hour}-{minute}.txt")

with open(log_file_name, 'w') as log_file:
    print(f'Тест начат {datetime.datetime.now()}', file=log_file)


def test_authorisation_by_email(selenium):
    # Позитивный тест авторизации по Email
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест позитивного сценария авторизации через email {datetime.datetime.now()}', file=LOG_FILE)
    page = AuthPage(selenium)
    page.btn_email_click()
    page.enter_username(EMAIL)
    page.enter_pass(PSSWRD)
    page.btn_auth_click()
    try:
        assert page.get_positive_lastname() == LASTNAME
        print('Тест позитивного сценария авторизации через email пройден')
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест позитивного сценария авторизации через email пройден', file=LOG_FILE)
    except AssertionError as AE:
        print(f'Тест позитивного сценария авторизации через email НЕ пройден по причине: \n    {AE}')
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест позитивного сценария авторизации через email НЕ пройден '
                  f'по причине: \n    {AE}', file=LOG_FILE)


def test_authorisation_by_phone(selenium):
    # Позитивный тест авторизации по номеру телефона
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест позитивного сценария авторизации через телефон {datetime.datetime.now()}', file=LOG_FILE)
    page = AuthPage(selenium)
    page.btn_phone_click()
    page.enter_username(PHONE)
    page.enter_pass(PSSWRD)
    page.btn_auth_click()
    try:
        assert page.get_positive_lastname() == LASTNAME
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест позитивного сценария авторизации через телефон пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест позитивного сценария авторизации через телефон НЕ пройден '
                  f'по причине: \n    {AE}', file=LOG_FILE)


def test_authorisation_by_login(selenium):
    # Позитивный тест авторизации по Логину
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест позитивного сценария авторизации через логин {datetime.datetime.now()}', file=LOG_FILE)
    page = AuthPage(selenium)
    page.btn_login_click()
    page.enter_username(LOGIN)
    page.enter_pass(PSSWRD)
    page.btn_auth_click()
    try:
        assert page.get_positive_lastname() == LASTNAME
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест позитивного сценария авторизации через логин пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест позитивного сценария авторизации через логин НЕ пройден '
                  f'по причине: \n    {AE}', file=LOG_FILE)


def test_authorisation_by_ls_negative(selenium):
    # Негативный тест авторизации по несуществующему номеру лицевого счёта
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест негативного сценария авторизации через лицевой счёт '
              f'(ЛС) {datetime.datetime.now()}', file=LOG_FILE)
    page = AuthPage(selenium)
    page.btn_ls_click()
    page.enter_username(LS)
    page.enter_pass(PSSWRD)
    page.btn_auth_click()
    try:
        assert page.get_error_message() == "Неверный логин или пароль"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест негативного сценария авторизации через ЛС пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест негативного сценария авторизации через ЛС НЕ пройден по причине: \n    {AE}', file=LOG_FILE)


def test_autodetect_phone_number(selenium):
    # Позитивный тест автоматической идентификации username как телефон
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест автоматической идентификации username как телефон {datetime.datetime.now()}', file=LOG_FILE)
    page = AuthPage(selenium)

    # Проверка на таб "Лицевой счёт"
    page.btn_ls_click()
    page.enter_username(PHONE)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Мобильный телефон"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию телефона в табе ЛС пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию телефона в табе ЛС НЕ пройден по причине: \n    {AE}', file=LOG_FILE)

    # Проверка на таб "Логин"
    page.btn_login_click()
    page.enter_username(PHONE)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Мобильный телефон"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию телефона в табе Логин пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию телефона в табе Логин НЕ пройден по причине: \n    {AE}', file=LOG_FILE)

    # Проверка на таб "Почта"
    page.btn_email_click()
    page.enter_username(PHONE)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Мобильный телефон"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию телефона в табе Почта пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию телефона в табе Почта НЕ пройден по причине: \n    {AE}', file=LOG_FILE)


def test_autodetect_email(selenium):
    # Позитивный тест автоматической идентификации username как email
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест автоматической идентификации username как email {datetime.datetime.now()}', file=LOG_FILE)
    page = AuthPage(selenium)

    # Проверка на таб "Лицевой счёт"
    page.btn_ls_click()
    page.enter_username(EMAIL)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Электронная почта"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию email в табе ЛС пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию email в табе ЛС НЕ пройден по причине: \n    {AE}', file=LOG_FILE)

    # Проверка на таб "Логин"
    page.btn_login_click()
    page.enter_username(EMAIL)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Электронная почта"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию email в табе Логин пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию email в табе Логин НЕ пройден по причине: \n    {AE}', file=LOG_FILE)

    # Проверка на таб "Телефон"
    page.btn_phone_click()
    page.enter_username(EMAIL)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Электронная почта"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию email в табе Телефон пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию email в табе Телефон НЕ пройден по причине: \n    {AE}', file=LOG_FILE)


def test_autodetect_login(selenium):
    # Позитивный тест автоматической идентификации username как Логин
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест автоматической идентификации username как Логин {datetime.datetime.now()}', file=LOG_FILE)
    page = AuthPage(selenium)

    # Проверка на таб "Лицевой счёт"
    page.btn_ls_click()
    page.enter_username(LOGIN)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Логин"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию логина в табе ЛС пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию логина в табе ЛС НЕ пройден по причине: \n    {AE}', file=LOG_FILE)

    # Проверка на таб "Почта"
    page.btn_email_click()
    page.enter_username(LOGIN)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Логин"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию логина в табе Почта пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию логина в табе Почта НЕ пройден по причине: \n    {AE}', file=LOG_FILE)

    # Проверка на таб "Телефон"
    page.btn_phone_click()
    page.enter_username(LOGIN)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Логин"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию логина в табе Телефон пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию логина в табе Телефон НЕ пройден по причине: \n    {AE}', file=LOG_FILE)


def test_autodetect_ls(selenium):
    # Позитивный тест автоматической идентификации username как Лицевой счёт
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест автоматической идентификации username как Лицевой счёт '
              f'(ЛС) {datetime.datetime.now()}', file=LOG_FILE)
    page = AuthPage(selenium)

    # Проверка на таб "Логин"
    page.btn_login_click()
    page.enter_username(LS)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Лицевой счёт"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию ЛС в табе Логин пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию ЛС в табе Логин НЕ пройден по причине: \n    {AE}', file=LOG_FILE)

    # Проверка на таб "Почта"
    page.btn_email_click()
    page.enter_username(LS)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Лицевой счёт"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию ЛC в табе Почта пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию ЛС в табе Почта НЕ пройден по причине: \n    {AE}', file=LOG_FILE)

    # Проверка на таб "Телефон"
    page.btn_phone_click()
    page.enter_username(LS)
    page.enter_pass(" ")
    try:
        assert page.get_username_placeholder() == "Лицевой счёт"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию ЛС в табе Телефон пройден', file=LOG_FILE)
    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест на идентификацию ЛС в табе Телефон НЕ пройден по причине: \n    {AE}', file=LOG_FILE)


def test_authorisation_by_code_to_email(selenium):
    # Позитивный тест авторизации по Коду на почту
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест позитивного сценария авторизации через код на почту {datetime.datetime.now()}', file=LOG_FILE)
    # Запуск страницы авторизации по коду и ввод email
    page = AuthCodePage(selenium)
    page.enter_ident(EMAIL)
    page.btn_get_code_click()

    try:
        # Проверка выполнения сценария по отправке кода
        assert page.get_title_input_code() == "Код подтверждения отправлен"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест отправки кода авторизации на почту пройден', file=LOG_FILE)
        # Запуск страницы почтового клиента, поиск письма и извлечение кода авторизации
        page2 = EmailPage(selenium)
        page2.enter_email_page()
        page2.driver.switch_to.window(page2.driver.window_handles[2])
        time.sleep(5)
        # Задержка на случай задержки письма
        page2.input_email_username(EMAIL)
        page2.save_username()
        page2.click_to_input_pass()
        page2.input_email_password(EMAIL_PASS)
        page2.click_to_enter_inbox_email()
        page2.first_mail_by_word("Код авторизации")
        mail_text = page2.get_first_mail_text()[9:15]
        page.driver.switch_to.window(page2.driver.window_handles[0])
        page.send_auth_code(mail_text)
        title_text = page
        try:
            # Проверка успешной авторизации по коду, отправленному на почту
            assert title_text == 'Ростелеком «Старт»' or 'https://start.rt.ru'
            with open(log_file_name, 'a') as LOG_FILE:
                print(f'Тест позитивного сценария авторизации через код на email пройден', file=LOG_FILE)
        except AssertionError as AE:
            with open(log_file_name, 'a') as LOG_FILE:
                print(f'Тест позитивного сценария авторизации через код на email НЕ пройден '
                      f'по причине: \n    {AE}', file=LOG_FILE)

    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест отправки кода авторизации на почту НЕ пройден по причине: \n    {AE}', file=LOG_FILE)


def test_authorisation_by_code_to_phone(selenium):
    # Позитивный тест авторизации по Коду на телефон
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест позитивного сценария авторизации через отправку кода '
              f'на телефон {datetime.datetime.now()}', file=LOG_FILE)
    # Запуск страницы авторизации по коду и ввод номера телефона
    page = AuthCodePage(selenium)
    page.enter_ident(PHONE)
    page.btn_get_code_click()

    try:
        # Проверка выполнения сценария по отправке кода
        assert page.get_title_input_code() == "Авторизация по коду"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест отправки кода авторизации на телефон пройден', file=LOG_FILE)

    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест отправки кода авторизации на телефон НЕ пройден по причине: \n    {AE}', file=LOG_FILE)


def test_registration_with_email(selenium):
    # Позитивный тест регистрации с электронной почтой
    with open(log_file_name, 'a') as LOG_FILE:
        print(f'\nТест позитивного сценария регистрации с электронной почтой {datetime.datetime.now()}', file=LOG_FILE)
    # Запуск страницы регистрации
    page = AuthPage(selenium)
    page.click_lnk_reg()
    # Переход к заполнению данных регистрации
    page.input_reg_name(NAME)
    page.input_reg_lastname(LASTNAME)
    page.input_reg_email(EMAIL2)
    page.input_reg_pass(PSSWRD)
    page.input_reg_pass_confirm(PSSWRD)
    page.click_btn_reg()
    time.sleep(5)
    try:
        # Проверка выполнения сценария по отправке кода подтверждения регистрации
        assert page.get_title_input_code() == "Подтверждение email"
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест отправки кода авторизации на почту пройден', file=LOG_FILE)
        # Запуск страницы почтового клиента, поиск письма и извлечение кода авторизации
        page2 = EmailPage(selenium)
        page2.enter_email_page()
        page2.driver.switch_to.window(page2.driver.window_handles[2])
        page2.input_email_username(EMAIL2)
        page2.save_username()
        page2.click_to_input_pass()
        page2.input_email_password(EMAIL_PASS)
        page2.click_to_enter_inbox_email()
        page2.first_mail_by_word("Регистрация в Ростелеком ID")
        mail_text = page2.get_first_mail_text()[10:16]
        page.driver.switch_to.window(page2.driver.window_handles[0])
        page.send_auth_code(mail_text)

        try:
            # Проверка успешной регистрации
            assert page.get_positive_lastname() == LASTNAME
            with open(log_file_name, 'a') as LOG_FILE:
                print(f'Тест позитивного сценария регистрации через код на email пройден', file=LOG_FILE)
        except AssertionError as AE:
            with open(log_file_name, 'a') as LOG_FILE:
                print(f'Тест позитивного сценария регистрации через код на email НЕ пройден '
                      f'по причине: \n    {AE}', file=LOG_FILE)

    except AssertionError as AE:
        with open(log_file_name, 'a') as LOG_FILE:
            print(f'Тест отправки кода авторизации на почту НЕ пройден по причине: \n    {AE}', file=LOG_FILE)
