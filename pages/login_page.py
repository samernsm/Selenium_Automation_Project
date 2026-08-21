from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import get_logger


class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    LOGIN_HEADING = (By.CSS_SELECTOR, "div.example h2")

    logger = get_logger(__name__)

    def login(self, username, password):
        self.logger.info("Starting login")

        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

        self.logger.info("Login button clicked")

    def get_flash_message(self):
        message = self.get_text(self.FLASH_MESSAGE)

        self.logger.info("Flash message: %s", message)

        return message
     
    def is_login_page_displayed(self):
        
        return self.find_visible(
            self.LOGIN_HEADING
        ).text == "Login Page"    
