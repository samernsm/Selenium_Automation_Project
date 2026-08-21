from pages.login_page import LoginPage


def test_logout(login_page, secure_page):
    login_page.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    heading = secure_page.get_heading()

    assert heading == "Secure Area"

    secure_page.logout()

    login_page = LoginPage(secure_page.driver)

    assert login_page.is_login_page_displayed()

    message = login_page.get_flash_message()

    assert "You logged out of the secure area!" in message
