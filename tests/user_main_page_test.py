import time

import pytest
import allure
from pages.user_main_page import UserMainPage
from pages.login_page import LoginPage
from conftest import driver


# @pytest.fixture(scope="session")
# def open_and_login(driver):
#     login_page = LoginPage(driver)
#     login_page.open_site()
#     login_page.login(username="thebazhenov@vk.com", password="servicemode")


def test_create_task(driver):
    """
    Функция создает задачу
    :param driver:
    :return:
    """
    login_page = LoginPage(driver)
    login_page.open_site()
    login_page.login(username="thebazhenov@vk.com", password="servicemode")
    user_main_page = UserMainPage(driver)
    user_main_page.create_task("AQA Test")

    assert user_main_page.check_notification


def test_set_admin_mode(driver):
    login_page = LoginPage(driver)
    login_page.open_site()
    login_page.login(username="thebazhenov@vk.com", password="servicemode")
    user_main_page = UserMainPage(driver)
    user_main_page.set_administrator_mode()

    assert user_main_page.check_admin_mode(), "Элемент активации режима администратора не найден"

