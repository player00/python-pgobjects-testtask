from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Optional


class BasePage:

    def __init__(self, driver, url: Optional[str] = None):
        self.driver = driver
        self.base_url = url or "http://automationpractice.com/index.php"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                        message=f"Can't find element by locator{locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
