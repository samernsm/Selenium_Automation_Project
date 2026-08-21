from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config.settings import BROWSER, HEADLESS


def create_driver():
    if BROWSER == "chrome":
        options = ChromeOptions()

        if HEADLESS:
            options.add_argument("--headless=new")

        options.add_argument("--window-size=1920,1080")

        return webdriver.Chrome(options=options)

    if BROWSER == "firefox":
        options = FirefoxOptions()

        if HEADLESS:
            options.add_argument("-headless")

        return webdriver.Firefox(options=options)

    raise ValueError(
        f"Unsupported browser: {BROWSER}. "
        "Supported browsers: chrome, firefox."
    )
