from pages.base_page import BasePage


class ProjectsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.project_menu_button = ("xpath", "//span[@class='sub__title elipsis' and text()='Проекты']")
        self.a_link_projects_menu = ("xpath", "//a[@routerlink='/projects']")
        self.create_project_button = ("xpath", "//button[@class='create-project-button cmf-button__primary']")
        self.create_project_button = ("xpath", "//button[@class='create-project-button cmf-button__primary']")
        self.agile_project_div = ("xpath", "//div[@class='project-node active ng-star-inserted']")
        # На данной кнопке будет всегда второй элемент
        self.next_button = ("xpath", "//span[@class='mat-button-wrapper' and text()='Далее']")

    def open_projects_menu(self):
        self.clickable(self.project_menu_button).click()
        self.clickable(self.a_link_projects_menu).click()

    def create_project(self):
        pass
