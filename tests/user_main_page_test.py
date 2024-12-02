import time

import pytest
import allure
from pages.user_main_page import UserMainPage
from pages.login_page import LoginPage
from conftest import driver


@pytest.fixture(scope="function")
def open_and_login(driver):
    login_page = LoginPage(driver)
    login_page.open_site()
    login_page.login(username="thebazhenov@vk.com", password="servicemode")

    return UserMainPage(driver)


def test_create_task(open_and_login):
    """
    Функция создает задачу
    :param open_and_login:
    :return:
    """
    user_main_page = open_and_login
    user_main_page.create_task()

    assert user_main_page.check_notification


def test_set_admin_mode(open_and_login):
    user_main_page = open_and_login
    user_main_page.set_administrator_mode()

    assert user_main_page.check_admin_mode(), "Элемент активации режима администратора не найден"


def test_create_personal_document(open_and_login):
    user_main_page = open_and_login
    user_main_page.create_document(name_document="IFAT 66")

    assert user_main_page.check_save_document


def test_delete_personal_document(open_and_login):
    user_main_page = open_and_login
    user_main_page.delete_person_document(name_document="IFAT 23")

    assert user_main_page.check_delete_document




