from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SecurePage(BasePage):

    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    SECURE_AREA_HEADING = (By.CSS_SELECTOR, "div.example h2")

    def get_heading(self):
        return self.get_text(self.SECURE_AREA_HEADING)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

