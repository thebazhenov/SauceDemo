from conftest import driver
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = ("xpath", "//input[@id='login']")
        self.password_field = ("xpath", "//input[@id='password']")
        self.login_button = ("xpath", "//button[@id='login-button']")
        self.exception_window = ("xpath", "//div[@id='error-message']")
        self.create_task_button = ("xpath", "//span[@class='trigger-menu-button-content']")

    @allure.step("Открытие страницы")
    def open_site(self) -> None:
        """
        Открывает сайт в браузере.
        :return: Ничего не возвращает.
        """
        self.driver.get(self.base_url)

    @allure.step("Авторизация на сайте")
    def login(self, username: str, password: str) -> None:
        """
        Метод для авторизации на сайте.

        :param username: Логин пользователя (строка).
        :param password: Пароль пользователя (строка).
        :return: Ничего не возвращает.
        """
        username_element = self.wait.until(EC.element_to_be_clickable(self.username_field))
        username_element.send_keys(username)

        password_element = self.wait.until(EC.element_to_be_clickable(self.password_field))
        password_element.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_button.click()

    @property
    def get_current_url(self) -> str:
        self.wait.until(EC.visibility_of_element_located(self.create_task_button)).is_displayed()
        return self.driver.current_url

    @property
    def get_error_message(self) -> str:
        """
        Метод для получения ошибки при авторизации
        :return: Возвращает текст ошибки
        """
        return self.wait.until(EC.visibility_of_element_located(self.exception_window)).is_displayed()