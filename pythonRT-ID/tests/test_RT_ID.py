from pages.auth_page import AuthPage

import time
import os
import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

LOGIN = os.environ.get("LOGIN")
PSSWRD = os.environ.get("PSSWRD")
PHONE = os.environ.get("PHONE")
EMAIL = os.environ.get("EMAIL")
LS = os.environ.get("LS")

def test_authorisation_by_email(selenium):
   #Позитивный тест авторизации по Email
   page = AuthPage(selenium)
   page.btn_email_click()
   page.enter_username(EMAIL)
   page.enter_pass(PSSWRD)
   page.btn_auth_click()
   assert page.get_positive_lastname() == "Иванов"

def test_authorisation_by_phone(selenium):
   #Позитивный тест авторизации по номеру телефона
   page = AuthPage(selenium)
   page.btn_phone_click()
   page.enter_username(PHONE)
   page.enter_pass(PSSWRD)
   page.btn_auth_click()
   assert page.get_positive_lastname() == "Иванов"

def test_authorisation_by_login(selenium):
   #Позитивный тест авторизации по Логину
   page = AuthPage(selenium)
   page.btn_login_click()
   page.enter_username(LOGIN)
   page.enter_pass(PSSWRD)
   page.btn_auth_click()
   assert page.get_positive_lastname() == "Иванов"

def test_authorisation_by_ls_negative(selenium):
   #Негативный тест авторизации по несуществующему номеру лицевого счёта
   page = AuthPage(selenium)
   page.btn_ls_click()
   page.enter_username(LS)
   page.enter_pass(PSSWRD)
   page.btn_auth_click()
   assert page.get_error_message() == "Неверный логин или пароль"

