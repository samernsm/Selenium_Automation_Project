# Selenium Automation Project

A Python-based web UI test automation framework built with Selenium WebDriver and Pytest.

The project demonstrates a maintainable automation framework using Page Object Model (POM), reusable fixtures, explicit waits, data-driven testing, logging, screenshots on test failure, and HTML test reports.

## Features

* Selenium WebDriver with Chrome
* Pytest test framework
* Page Object Model (POM)
* Reusable `BasePage`
* Pytest fixtures
* Explicit waits
* Data-driven testing with `pytest.mark.parametrize`
* Automatic screenshots on test failure
* Test logging
* HTML test reports
* Separate test data and configuration
* Git/GitHub integration

## Tech Stack

* Python 3.13
* Selenium 4.47.0
* Pytest 9.1.1
* pytest-html
* Chrome WebDriver
* Git / GitHub

## Project Structure

```text
Selenium_Automation_Project/
│
├── config/
│   └── settings.py
│
├── data/
│   └── login_data.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── secure_page.py
│   └── home_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_logout.py
│
├── utils/
│   ├── driver_factory.py
│   └── logger.py
│
├── screenshots/
├── logs/
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Coverage

The current test suite covers:

| Test Case           | Description                                             |
| ------------------- | ------------------------------------------------------- |
| Valid Login         | Verifies successful login with valid credentials        |
| Invalid Credentials | Verifies login rejection with invalid credentials       |
| Empty Username      | Verifies validation when username is empty              |
| Empty Password      | Verifies validation when password is empty              |
| Logout              | Verifies successful logout and return to the login page |

Current result:

```text
5 passed
```

## Installation

Clone the repository:

```bash
git clone https://github.com/samernsm/Selenium_Automation_Project.git
cd Selenium_Automation_Project
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run Tests

Run the complete test suite:

```powershell
pytest -v
```

## Generate HTML Test Report

Create the `reports` directory if it does not exist:

```powershell
mkdir reports
```

Generate the HTML report:

```powershell
pytest -v --html=reports/report.html --self-contained-html
```

The generated report will be available at:

```text
reports/report.html
```

## Failure Screenshots

When a test fails, the framework automatically captures a screenshot and stores it in:

```text
screenshots/
```

Example:

```text
screenshots/test_login.png
```

Generated screenshots are excluded from Git using `.gitignore`.

## Logging

The framework records test-related events in:

```text
logs/test.log
```

Example log entries include:

```text
INFO - pages.login_page - Starting login
INFO - pages.login_page - Login button clicked
INFO - pages.login_page - Flash message: You logged into a secure area!
```

Generated log files are excluded from Git.

## Architecture

The framework separates responsibilities between different layers:

```text
Tests
  ↓
Page Objects
  ↓
BasePage
  ↓
Selenium WebDriver
```

### Tests

Contains test cases and assertions.

### Page Objects

Contains page locators and page-specific actions.

### BasePage

Contains reusable Selenium operations such as:

* Finding visible elements
* Waiting for clickable elements
* Clicking elements
* Entering text
* Reading element text

### Fixtures

`conftest.py` manages reusable test dependencies such as the WebDriver and Page Objects.

### Test Data

Login test data is separated from test logic in:

```text
data/login_data.py
```

## Example

A data-driven login test uses the same test logic with multiple datasets:

```python
@pytest.mark.parametrize(
    "username, password, expected_message",
    LOGIN_TEST_DATA,
)
def test_login(login_page, username, password, expected_message):
    login_page.login(username, password)

    message = login_page.get_flash_message()

    assert expected_message in message
```

## Future Improvements

Planned improvements include:

* More authentication test cases
* Additional Page Objects
* Cross-browser testing
* Browser configuration
* Parallel test execution
* CI/CD integration
* Improved reporting
* API test integration

## Author

**Samer Nabil**

GitHub:

https://github.com/samernsm

## License

This project is intended for learning, demonstration, and portfolio purposes.

```
```
