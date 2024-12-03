import pytest
from pages.projects_page import ProjectsPage
from pages.login_page import LoginPage
from conftest import driver


@pytest.fixture(scope="function")
def open_and_login(driver):
    login_page = LoginPage(driver)
    login_page.open_site()
    login_page.login(username="thebazhenov@vk.com", password="servicemode")

    return ProjectsPage(driver)


def open_menu_projects(open_and_login):
    project_page = open_and_login

