import pytest

from data.login_data import LOGIN_TEST_DATA


@pytest.mark.parametrize(
    "username, password, expected_message",
    LOGIN_TEST_DATA,
)
def test_login(login_page, username, password, expected_message):
    login_page.login(username, password)

    message = login_page.get_flash_message()

    assert expected_message in message