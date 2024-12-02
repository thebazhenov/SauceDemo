from conftest import driver
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


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

    def create_task(self, name_task: str) -> None:
        self.clickable(self.create_button).click()
        self.visibility(self.window_task)
        self.clickable(self.task_name_field).send_keys(name_task)
        self.clickable(self.check_button).click()
        self.clickable(self.span_sv).click()
        self.clickable(self.responsible_field).click()
        self.clickable(self.responsible_user).click()
        self.clickable(self.create_task_button).click()

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




