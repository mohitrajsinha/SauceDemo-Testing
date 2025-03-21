﻿# sauceDemo Testing

This project is an automated testing suite for the SauceDemo website using Selenium and pytest. The tests cover various functionalities such as login, adding items to the cart, and logging out.

## Project Structure

- `pages/`: Contains page object classes for different pages of the website.
- `tests/`: Contains test cases for different functionalities.
- `utils/`: Contains utility functions and constants.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/mohitrajsinha/syfe-saucedemo-assignment.git
    cd syfe-saucedemo-assignment
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Tests

1. **Run all tests:**

    ```sh
    python -m pytest
    ```

2. **Run tests and generate an HTML report:**

    ```sh
    python -m pytest --html=reports/test_report.html
    ```

3. **Run a specific test file:**

    ```sh
    python -m pytest tests/test_login.py
    ```

## Test Cases

- **Login Tests:**
  - `test_valid_login`: Verifies that a user can log in with valid credentials.
  - `test_invalid_login`: Verifies that an error message is displayed for invalid login credentials.
  - `test_empty_credentials`: Verifies that an error message is displayed when no credentials are provided.

- **Add to Cart Tests:**
  - `test_add_items_to_cart`: Verifies that items can be added to the cart and are displayed correctly.

- **Logout Tests:**
  - `test_logout`: Verifies that a user can log out and is redirected to the login page.

## Notes

- Ensure that the `chromedriver` executable is in your PATH or in the project directory.
- Update the `VALID_USERNAME`, `VALID_PASSWORD`, `INVALID_USERNAME`, and `INVALID_PASSWORD` constants in [constants.py](http://_vscodecontentref_/1) with appropriate values.
