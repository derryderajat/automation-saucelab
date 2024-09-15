# Saucedemo E-commerce Automation Testing

This project is an automated testing suite for the [Sauce Demo](https://www.saucedemo.com) e-commerce application. The test suite is built using Selenium WebDriver, pytest, and Python, covering key functionalities like user login and product interactions.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Test Structure](#test-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project automates testing for the [Sauce Demo](https://www.saucedemo.com) application, focusing on login functionalities and user interactions with products. The test scenarios cover both positive and negative cases for:

- User login
- Adding items to the cart
- Checking out items
- Navigating the website

## Technologies

- **Python 3.12.x**
- **Selenium WebDriver**
- **pytest**
- **WebDriver Manager**
- **dotenv** (for managing environment variables)

## Installation

### Prerequisites

Ensure the following are installed on your system:

- Python 3.x
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/derryderajat/automation-saucelab.git
cd automation-saucelab
```

### Create and Activate Virtual Environment

For **macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

For **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Environment Variables

Create a `.env` file to manage your environment variables (if required). Example of `.env` file contents:

```
BASE_URL=https://www.saucedemo.com
```

## Running the Tests

You can run the tests using pytest. The default test scenario runs against the Sauce Demo login page.

### Basic Test Run

```bash
pytest
```

### Running Tests with Specific Browsers

You can specify which browser to use with the `--browser` option. Supported browsers are `chrome`, `firefox`, `edge`, `safari`, and `ie`.

For example, to run the tests in **Chrome**:

```bash
pytest --browser chrome
```

### Running in Headless Mode

If you prefer to run the tests in headless mode (without opening a browser window):

```bash
pytest --headless
```

### Generating HTML Reports

You can generate HTML reports for the test results with:

```bash
pytest --html=report.html
```

## Test Structure

The project uses the **Page Object Model (POM)** design pattern to maintain clean and readable code. Below is the directory structure:

```plaintext
saucedemo-automation/
│
├── locators/                # Contains element locators for different pages
│   ├── auth_locators.py     # Locators for the login page
│
├── pages/                   # Contains page objects for interacting with the UI
│   ├── auth/                # Authentication-related pages
│   │   └── login_page.py    # Page object for login interactions
│
├── tests/                   # Test files
│   ├── ui/                  # UI-based test cases
│   │   └── test_login.py    # Tests for login functionality
│   ├── conftest.py          # Test configuration and fixtures
│
├── utils/                   # Utility functions for common operations
│   └── ui_utils.py          # Helper functions (e.g., waits, assertions)
│   ├── login_util.py        # Helper for login perform
│
├── .env                     # Environment variables file (optional)
├── pytest.ini               # pytest configuration file
├── requirements.txt         # List of project dependencies
└── README.md                # Project documentation
```

## Example Test Case

Here is a simple login test for `saucedemo.com`:

```python
import pytest
from time import sleep
from pages.auth.login_page import LoginPage

@pytest.mark.usefixtures("init_driver")
class TestLogin:
    BASE_URL = "https://www.saucedemo.com"

    def setup_method(self):
        self.driver.get(self.BASE_URL)
        self.page = LoginPage(self.driver, self.wait)
    
    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
    def test_login_valid(self, username, password):
        self.page.action_login(username, password)
        sleep(3)
        assert self.page.utils.is_on_page("inventory")
```

This test logs in with valid credentials (`standard_user`, `secret_sauce`) and verifies navigation to the inventory page.

## Contributing

Contributions are welcome! Feel free to submit a pull request with improvements or bug fixes.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a Pull Request.

