from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)
        self.base_url = "https://thebazhenov.su/"

    def clickable(self, locator: tuple):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def visibility(self, locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(locator))