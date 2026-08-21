import os


BASE_URL = os.getenv(
    "BASE_URL",
    "https://the-internet.herokuapp.com",
)

LOGIN_URL = f"{BASE_URL}/login"

BROWSER = os.getenv("BROWSER", "chrome").lower()

HEADLESS = os.getenv(
    "HEADLESS",
    "false",
).lower() == "true"

