Для успешного тестирования проекта Ростелеком-ID необходимо:

1. Установитm(скачать) драйвер selenium.Chrome c соответствующей версией браузера.
ссылка для скачивания - https://chromedriver.chromium.org/downloads

2. Распаковать архив с драйвером (желательно в корень одного из дисков)

3. Создать новый Python-проект (Проверено в PyCharm)

4. Скопировать в папку с проектом содержимое репозитория, а именно:
- папка tests
- папка pages
- файл .env

5. Изменить настройки для проекта в PyCharm:
File->Settings->Tools->Python Integrated Tools
Параметр "Default test runner" установить "pytest"

6. В терминале последовательно запустить следующие комманды для установки необходимых библиотек:
pip install pytest
pip install pytest-dotenv
pip install pytest-selenium

7. Для запуска тестирования в терминале необходимо использовать комманду:
python -m pytest -v --driver Chrome --driver-path <путь к файлу драйвера>\chromedriver.exe  tests\test_RT_ID.py

ВАЖНО!!!!!
1. Во время прохождения тестов в папке с проектом создаётся (при первом тестировании) директория "logs",
в которую записывается файл с полным логом тестирования и описанием параметров, которые не прошли тот
или иной тест.
2. Последний тест, на регистрацию, пройдёт только один раз, затем EMAIL2 будет занят и для нового успешного прохождения
нужно будет регистрировать на mail.ru новый почтовый ящик и указывать его в параметре EMAIL2 файла .env