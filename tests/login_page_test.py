import time

import pytest
import allure
from pages.login_page import LoginPage


@allure.title("Авторизация с корректными параметрами")
def test_correct_login(driver):
    login_page = LoginPage(driver)
    login_page.open_site()
    login_page.login(username="thebazhenov@vk.com", password="servicemode")
    assert login_page.get_current_url == "https://thebazhenov.su/desk/cards"


@pytest.mark.parametrize(
    "username, password, exception",
    [
        ("locked_out_user", "secret_sauce", "Неверный логин или пароль. "),
        ("", "secret_sauce", "Неверный логин или пароль. "),
        ("standart_user", "", "Неверный логин или пароль. "),
        ("", "", "Неверный логин или пароль. ")
    ]
)
@allure.title("Авторизация с некорректными параметрами")
def test_uncorrected_login(driver, username, password, exception):
    login_page = LoginPage(driver)
    login_page.open_site()
    login_page.login(username=username, password=password)
    print(login_page.get_error_message)

    assert login_page.get_error_message == True
