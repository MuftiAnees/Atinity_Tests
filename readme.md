# Atinity Solutions Website Test Cases

This repository contains automated test cases for the Atinity Solutions website. The tests are written in Python using the Selenium framework and pytest.

## Table of Contents

* [Introduction](#introduction)
* [Test Cases](#test-cases)
* [Getting Started](#getting-started)
* [Running the Tests](#running-the-tests)
* [Contributing](#contributing)
* [License](#license)

## Introduction

Atinity Solutions is a leading provider of innovative technology solutions. These test cases are designed to ensure the quality and functionality of their website. The tests cover various aspects of the website, including:

* Navigation and links
* Form submissions
* Content validation
* Responsiveness

## Test Cases

The following test cases are currently implemented:

* **Homepage:**
    * Verify the page title.
    * Verify the main navigation menu items.
    * Verify the presence of key elements (logo, hero image, etc.).
* **About Us Page:**
    * Verify the page title.
    * Verify the presence of company information.
* **Contact Us Page:**
    * Verify the form fields.
    * Submit the form and verify the success message.
* **Services Pages:**
    * Verify the page titles for each service.
    * Verify the presence of service descriptions.

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/MuftiAnees/Atinity_Tests](https://www.google.com/search?q=https://github.com/MuftiAnees/Atinity_Tests)
    ```

2.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your testing environment:**
    * Ensure you have a compatible web browser installed (I am using Edge for testing).
    * The `webdriver-manager` package will automatically handle the necessary WebDriver installations.

## Running the Tests

1.  **Open a terminal** in the project directory.
2.  **Run the tests** using pytest:

    ```bash
    pytest
    ```

    * You can also generate an HTML report:

    ```bash
    pytest --html=report.html
    ```

## Contributing

Contributions are welcome! If you find any issues or want to add new test cases, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.