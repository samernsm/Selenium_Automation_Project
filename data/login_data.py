import pytest


LOGIN_TEST_DATA = [
    pytest.param(
        "tomsmith",
        "SuperSecretPassword!",
        "You logged into a secure area!",
        id="valid_login",
    ),
    pytest.param(
        "wrong_user",
        "wrong_password",
        "Your username is invalid!",
        id="invalid_credentials",
    ),
    pytest.param(
        "",
        "SuperSecretPassword!",
        "Your username is invalid!",
        id="empty_username",
    ),
    pytest.param(
        "tomsmith",
        "",
        "Your password is invalid!",
        id="empty_password",
    ),
]