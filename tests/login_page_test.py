import pytest
import allure
from pages.login_page import LoginPage

@allure.title("Авторизация с корректными параметрами")
def test_correct_login(driver):
    login_page = LoginPage(driver)
    login_page.open_site()
    login_page.login(username="standard_user", password="secret_sauce")

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

@pytest.mark.parametrize(
    "username, password, exception",
    [
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standart_user", "", "Epic sadface: Password is required"),
        ("", "", "Epic sadface: Username is required")
    ]
)
@allure.title("Авторизация с некорректными параметрами")
def test_uncorrected_login(driver, username, password, exception):
    login_page = LoginPage(driver)
    login_page.open_site()
    login_page.login(username=username, password=password)

    assert login_page.get_error_message == exception