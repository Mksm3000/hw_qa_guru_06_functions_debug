from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения тёмной темы на сайте в зависимости от
    времени.
    """
    current_time = time(hour=23)
    is_dark_theme = None

    if time(hour=6) <= current_time < time(hour=22):
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от
    времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется
    переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    is_dark_theme = None

    if dark_theme_enabled_by_user:
        is_dark_theme = True
    elif not dark_theme_enabled_by_user:
        is_dark_theme = False
    elif dark_theme_enabled_by_user is None:
        if time(hour=6) <= current_time < time(hour=22):
            is_dark_theme = False
        else:
            is_dark_theme = True

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = dict()

    for user in users:
        if user["name"] == "Olga":
            suitable_users.update(user)

    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = list()

    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать читаемое имя переданной ей функции и
# значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву),
# затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome") "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login",
                                           button_text="Register")


def print_function_name_and_args(function_name, *args):
    func_name = function_name.__name__.replace("_", " ").title()
    text = ", ".join([arg for arg in args])
    return f'{func_name} [{text}]'


def open_browser(browser_name):
    actual_result = print_function_name_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_name_and_args(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_name_and_args(
        find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == ("Find Registration Button On Login Page ["
                             "https://companyname.com/login, Register]")