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

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

if os.path.exists('logs'):
   log_file_name = str(f"logs\\log_{datetime.date.today()}-{hour}-{minute}.txt")
else:
   os.mkdir('logs')
   log_file_name = str(f"logs\\log_{datetime.date.today()}-{hour}-{minute}.txt")

with open(log_file_name,'w') as log_file:
    print(f'Тест начат {datetime.datetime.now()}', file=log_file)

# def test_authorisation_by_email(selenium):
#    #Позитивный тест авторизации по Email
#    with open(log_file_name, 'a') as log_file:
#       print(f'\nТест позитивного сценария авторизации через email {datetime.datetime.now()}', file=log_file)
#    page = AuthPage(selenium)
#    page.btn_email_click()
#    page.enter_username(EMAIL)
#    page.enter_pass(PSSWRD)
#    page.btn_auth_click()
#    try:
#       assert page.get_positive_lastname() == "Иванов"
#       print('Тест позитивного сценария авторизации через email пройден')
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест позитивного сценария авторизации через email пройден', file=log_file)
#    except AssertionError as AE:
#       print(f'Тест позитивного сценария авторизации через email НЕ пройден по причине: \n    {AE}')
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест позитивного сценария авторизации через email НЕ пройден по причине: \n    {AE}', file=log_file)
#
#
# def test_authorisation_by_phone(selenium):
#    #Позитивный тест авторизации по номеру телефона
#    with open(log_file_name, 'a') as log_file:
#       print(f'\nТест позитивного сценария авторизации через телефон {datetime.datetime.now()}', file=log_file)
#    page = AuthPage(selenium)
#    page.btn_phone_click()
#    page.enter_username(PHONE)
#    page.enter_pass(PSSWRD)
#    page.btn_auth_click()
#    try:
#       assert page.get_positive_lastname() == "Иванов"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест позитивного сценария авторизации через телефон пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест позитивного сценария авторизации через телефон НЕ пройден по причине: \n    {AE}', file=log_file)
#
# def test_authorisation_by_login(selenium):
#    #Позитивный тест авторизации по Логину
#    with open(log_file_name, 'a') as log_file:
#       print(f'\nТест позитивного сценария авторизации через логин {datetime.datetime.now()}', file=log_file)
#    page = AuthPage(selenium)
#    page.btn_login_click()
#    page.enter_username(LOGIN)
#    page.enter_pass(PSSWRD)
#    page.btn_auth_click()
#    try:
#       assert page.get_positive_lastname() == "Иванов"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест позитивного сценария авторизации через логин пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест позитивного сценария авторизации через логин НЕ пройден по причине: \n    {AE}', file=log_file)
#
# def test_authorisation_by_ls_negative(selenium):
#    #Негативный тест авторизации по несуществующему номеру лицевого счёта
#    with open(log_file_name, 'a') as log_file:
#       print(f'\nТест негативного сценария авторизации через лицевой счёт (ЛС) {datetime.datetime.now()}', file=log_file)
#    page = AuthPage(selenium)
#    page.btn_ls_click()
#    page.enter_username(LS)
#    page.enter_pass(PSSWRD)
#    page.btn_auth_click()
#    try:
#       assert page.get_error_message() == "Неверный логин или пароль"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест негативного сценария авторизации через ЛС пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест негативного сценария авторизации через ЛС НЕ пройден по причине: \n    {AE}', file=log_file)
#
# def test_autodetect_phone_number(selenium):
#    #Позитивный тест автоматической идентификации username как телефон
#    with open(log_file_name, 'a') as log_file:
#       print(f'\nТест автоматической идентификации username как телефон {datetime.datetime.now()}', file=log_file)
#    page =AuthPage(selenium)
#
#    #Проверка на таб "Лицевой счёт"
#    page.btn_ls_click()
#    page.enter_username(PHONE)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder()=="Мобильный телефон"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию телефона в табе ЛС пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию телефона в табе ЛС НЕ пройден по причине: \n    {AE}', file=log_file)
#
#    # Проверка на таб "Логин"
#    page.btn_login_click()
#    page.enter_username(PHONE)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder() == "Мобильный телефон"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию телефона в табе Логин пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию телефона в табе Логин НЕ пройден по причине: \n    {AE}', file=log_file)
#
#    #Проверка на таб "Почта"
#    page.btn_email_click()
#    page.enter_username(PHONE)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder() == "Мобильный телефон"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию телефона в табе Почта пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию телефона в табе Почта НЕ пройден по причине: \n    {AE}', file=log_file)
#
# def test_autodetect_email(selenium):
#    #Позитивный тест автоматической идентификации username как email
#    with open(log_file_name, 'a') as log_file:
#       print(f'\nТест автоматической идентификации username как email {datetime.datetime.now()}', file=log_file)
#    page =AuthPage(selenium)
#
#    #Проверка на таб "Лицевой счёт"
#    page.btn_ls_click()
#    page.enter_username(EMAIL)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder()=="Электронная почта"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию email в табе ЛС пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию email в табе ЛС НЕ пройден по причине: \n    {AE}', file=log_file)
#
#    # Проверка на таб "Логин"
#    page.btn_login_click()
#    page.enter_username(EMAIL)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder() == "Электронная почта"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию email в табе Логин пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию email в табе Логин НЕ пройден по причине: \n    {AE}', file=log_file)
#
#    #Проверка на таб "Телефон"
#    page.btn_phone_click()
#    page.enter_username(EMAIL)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder() == "Электронная почта"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию email в табе Телефон пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию email в табе Телефон НЕ пройден по причине: \n    {AE}', file=log_file)
#
# def test_autodetect_login(selenium):
#    #Позитивный тест автоматической идентификации username как Логин
#    with open(log_file_name, 'a') as log_file:
#       print(f'\nТест автоматической идентификации username как Логин {datetime.datetime.now()}', file=log_file)
#    page =AuthPage(selenium)
#
#    #Проверка на таб "Лицевой счёт"
#    page.btn_ls_click()
#    page.enter_username(LOGIN)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder()=="Логин"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию логина в табе ЛС пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию логина в табе ЛС НЕ пройден по причине: \n    {AE}', file=log_file)
#
#    # Проверка на таб "Почта"
#    page.btn_email_click()
#    page.enter_username(LOGIN)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder() == "Логин"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию логина в табе Почта пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию логина в табе Почта НЕ пройден по причине: \n    {AE}', file=log_file)
#
#    #Проверка на таб "Телефон"
#    page.btn_phone_click()
#    page.enter_username(LOGIN)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder() == "Логин"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию логина в табе Телефон пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию логина в табе Телефон НЕ пройден по причине: \n    {AE}', file=log_file)
#
# def test_autodetect_ls(selenium):
#    #Позитивный тест автоматической идентификации username как Лицевой счёт
#    with open(log_file_name, 'a') as log_file:
#       print(f'\nТест автоматической идентификации username как Лицевой счёт (ЛС) {datetime.datetime.now()}', file=log_file)
#    page =AuthPage(selenium)
#
#    #Проверка на таб "Логин"
#    page.btn_login_click()
#    page.enter_username(LS)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder()=="Лицевой счёт"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию ЛС в табе Логин пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию ЛС в табе Логин НЕ пройден по причине: \n    {AE}', file=log_file)
#
#    # Проверка на таб "Почта"
#    page.btn_email_click()
#    page.enter_username(LS)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder() == "Лицевой счёт"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию ЛC в табе Почта пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию ЛС в табе Почта НЕ пройден по причине: \n    {AE}', file=log_file)
#
#    #Проверка на таб "Телефон"
#    page.btn_phone_click()
#    page.enter_username(LS)
#    page.enter_pass(" ")
#    try:
#       assert page.get_username_placeholder() == "Лицевой счёт"
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию ЛС в табе Телефон пройден', file=log_file)
#    except AssertionError as AE:
#       with open(log_file_name, 'a') as log_file:
#          print(f'Тест на идентификацию ЛС в табе Телефон НЕ пройден по причине: \n    {AE}', file=log_file)

def test_authorisation_by_code_to_email(selenium):
   #Позитивный тест авторизации по Коду на почту
   with open(log_file_name, 'a') as log_file:
      print(f'\nТест позитивного сценария авторизации через код на почту {datetime.datetime.now()}', file=log_file)
   page = AuthCodePage(selenium)
   page.enter_ident(EMAIL)
   page.btn_get_code_click()
   time.sleep(3)

   try:
      assert page.get_title_input_code() == "Код подтверждения отправлен"
      with open(log_file_name, 'a') as log_file:
         print(f'Тест отправки кода авторизации на почту пройден', file=log_file)
      page2 = EmailPage(selenium)
      page2.enter_email_page()
      time.sleep(5)
      page2.input_email_username()

   except AssertionError as AE:
      with open(log_file_name, 'a') as log_file:
         print(f'Тест отправки кода авторизации на почту НЕ пройден по причине: \n    {AE}', file=log_file)




