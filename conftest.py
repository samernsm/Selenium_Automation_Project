import os
from pathlib import Path

import pytest
 
from utils.driver_factory import create_driver
from config.settings import LOGIN_URL
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


SCREENSHOTS_DIR = Path("screenshots")


@pytest.fixture
def driver():
    driver = create_driver()

    yield driver

    driver.quit()


@pytest.fixture
def login_page(driver):
    driver.get(LOGIN_URL)
    return LoginPage(driver)


@pytest.fixture
def secure_page(driver):
    return SecurePage(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is not None:
            SCREENSHOTS_DIR.mkdir(exist_ok=True)

            screenshot_path = (
                SCREENSHOTS_DIR / f"{item.name}.png"
            )

            driver.save_screenshot(str(screenshot_path))

