from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            10,
            ignored_exceptions=(StaleElementReferenceException,),
        )

    def find_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text):
        self.find_visible(locator).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(
            lambda driver: driver.find_element(*locator).text
        )

