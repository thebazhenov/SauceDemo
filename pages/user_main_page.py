from selenium.webdriver.remote.webelement import WebElement

from conftest import driver
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time


class UserMainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.create_button = ("xpath", "//span[@class='trigger-menu-button-content']")
        self.task_name_field = ("xpath", "//textarea[@id='inline_edit_string_input']")
        self.responsible_field = ("xpath", "//div[@class='person-render-content']")
        self.window_task = ("xpath", "//div[@class='toolbar']")
        self.check_button = ("xpath", "//span[@class='mat-button-wrapper']/app-cmf-icon[@class='check']")
        self.responsible_user = ("xpath", "//div/span[@title='thebazhenov']")
        self.create_task_button = ("xpath", "//button[@class='dummy-save-btn cmf-button__primary']")
        self.span_sv = ("xpath", "//div[@class='expansion-panel-header']/span[text()='Сведения']")
        self.div_notification = ("xpath", "//div[@class='notify-card active ng-star-inserted']")
        self.user_icon = ("xpath", "//div[@class='app-gravatar']")
        self.set_administrator_span = ("xpath", "//span[@class='mat-focus-indicator acl-admin-mode-state mat-menu-item ng-star-inserted']")
        self.span_administrator = ("xpath", "//span[@class='user-alarm-title ng-star-inserted']")
        self.menu_button_arrow = ("xpath", "//span[@class='trigger-menu-button-arrow']")
        self.menu_button_add = ("xpath", "//span[text() = 'Добавить в меню']")
        self.document = ("xpath", "//*[contains(text(),'Создать личный документ')]")
        self.document_name_field = ("xpath", "//input[@placeholder='Имя документа']")
        self.span_ready_for_document = ("xpath", "//span[@class='mat-button-wrapper' and text()='Готово']")
        self.save_document_window = ("xpath", "//*[contains(text(), 'Сохранение...')]")
        self.find_document_delete = ()
        self.setting_document = ("xpath", "//button[@class='mat-tooltip-trigger mat-menu-trigger action']")
        self.button_delete_document = ("xpath", "//button[@role='menuitem' and text()='Удалить']")
        self.modal_question_window = ("xpath", "//div[@class='modal-question__wrap']")
        self.modal_question_window_yes = ("xpath", "//span[@class='mat-button-wrapper' and text()='Да']")
        self.check_window_delete = ("xpath", "//div[@class='document normal-screen ng-star-inserted']/*[contains(text(), 'Удалено')]")
        self.person_documents = ("xpath", "//a[@class='left-lists__menu__item ng-star-inserted']")

    def create_task(self, name_task: str = "AQA Test") -> None:
        """
        Метод создает задачу через кнопку "Создать" в верхнем тулбаре
        :param name_task: Наименование задачи
        :return:
        """
        self.clickable(self.create_button).click()
        self.visibility(self.window_task)
        self.clickable(self.task_name_field).send_keys(name_task)
        self.clickable(self.check_button).click()
        self.clickable(self.span_sv).click()
        self.clickable(self.responsible_field).click()
        self.clickable(self.responsible_user).click()
        self.clickable(self.create_task_button).click()

    def create_document(self, name_document: str = "AQA Document") -> None:
        """
        Метод создает документ через кнопку "Создать" в верхнем тулбаре
        :param name_document:
        :return:
        """
        self.clickable(self.menu_button_arrow).click()
        add_element_hover = self.clickable(self.menu_button_add)
        self.clickable(add_element_hover).click()
        self.clickable(self.document).click()
        self.clickable(self.document_name_field).send_keys(name_document)
        self.clickable(self.span_ready_for_document).click()
        time.sleep(5)

    def delete_person_document(self, document: WebElement) -> bool:
        """
        Метод удаляет все персональные документы на главной странице пользователя
        :param document: Вебэлемент от find.element
        :return: Возвращает True | False в зависимости от успешности
        """
        try:
            # self.find_document_delete = ("xpath", f"//div[@class='mat-tooltip-trigger left-lists__menu__item__title' and text()={name_document}]")
            self.visibility(self.document).click()
            self.clickable(self.setting_document).click()
            self.clickable(self.button_delete_document).click()
            self.visibility(self.modal_question_window)
            self.clickable(self.modal_question_window_yes).click()
            return True
        except Exception as e:
            print(f'Встретилась ошибка при попытке удалить документ: {e}')
            return False

    @property
    def check_delete_document(self) -> bool:
        """
        Проверяет удаление элемента через модальное окно
        :return: bool True | False в зависимости от успешности
        """
        try:
            return self.visibility(self.check_window_delete).is_displayed()
        except Exception as e:
            print(f"Ошибка при попытке найти окно сохранения: {e}")
            return False

    @property
    def check_save_document(self) -> bool:
        """
        
        :return:
        """
        try:
            return self.visibility(self.save_document_window).is_displayed()
        except Exception as e:
            print(f"Ошибка при попытке найти окно сохранения: {e}")
            return False

    @property
    def check_notification(self):
        return self.wait.until(EC.visibility_of_element_located(self.div_notification)).is_displayed()

    def set_administrator_mode(self):
        self.clickable(self.user_icon).click()
        self.clickable(self.set_administrator_span).click()

    def check_admin_mode(self):
        try:
            return self.visibility(self.span_administrator).is_displayed()
        except Exception as e:
            print(f"Ошибка при попытке найти активацию режима администратора: {e}")
            return False

    def delete_all_person_document(self):
        try:
            documents = self.finds(self.person_documents)
            for document in documents:
                self.visibility(document).click()
                self.clickable(self.setting_document).click()
                self.clickable(self.button_delete_document).click()
                self.visibility(self.modal_question_window)
                self.clickable(self.modal_question_window_yes).click()
            return True
        except Exception as e:
            print(f"Встретилась ошибка {e}")
            return False



