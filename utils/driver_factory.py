from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.settings import BROWSER, HEADLESS


def create_driver():
    if BROWSER != "chrome":
        raise ValueError(
            f"Unsupported browser: {BROWSER}. "
            "Currently supported: chrome."
        )

    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(options=options)

