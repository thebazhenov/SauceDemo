from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920, 1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("""
    --user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) 
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 
    YaBrowser/24.10.0.0 Safari/537.36
                                """)
    serivce = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=serivce, options=chrome_options)

    return driver
