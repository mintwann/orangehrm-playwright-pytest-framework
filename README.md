# OrangeHRM Hybrid Test Automation Framework

A professional-grade Hybrid Test Automation Framework designed for the OrangeHRM (Open Source v5.x) web application. This project demonstrates modern automation engineering practices, combining UI and API testing to achieve fast, robust, and scalable test execution.

---

## Key Features

- **Hybrid Testing Approach**: Speeds up execution by using API requests for test data setup (pre-requisites) and teardown (cleanup), reserving UI automation solely for high-value user scenarios.
- **Page Object Model (POM)**: Implemented using custom wrappers over Playwright for highly maintainable and readable UI actions.
- **Robust API Client**: A lightweight wrapper around Python's `requests` library with integrated logging and error handling.
- **Configuration Management**: Centralized environment configuration using `.env` and `config.ini` files to ensure seamless switching between Dev, Staging, and Production environments.
- **Rich Reporting**: Integrated with Allure Report to generate interactive HTML reports, automatically capturing screenshots and logs upon failure.
- **CI/CD Pipeline**: GitHub Actions workflow that automatically executes tests in headless browsers and deploys Allure Reports directly to GitHub Pages.
- **Dockerized Execution**: Dockerfile configuration allowing tests to run in an isolated and consistent environment.

---

## Tech Stack

- **Language**: Python 3.11+
- **Test Runner**: Pytest
- **UI Engine**: Playwright (with `pytest-playwright` plugin)
- **API Engine**: Requests
- **Reporting**: Allure Report
- **CI/CD**: GitHub Actions & GitHub Pages
- **Containerization**: Docker

---

## Project Structure

```text
orangehrm-playwright-pytest-framework/
├── .github/
│   └── workflows/
│       └── run-tests.yml        # CI/CD Workflow Configuration
├── config/
│   ├── config.ini               # Base Framework Configurations
│   └── settings.py              # Environment Loader (.env reader)
├── data/
│   └── test_data.json           # Decentralized Test Input Data
├── pages/                       # UI Page Object Classes
│   ├── __init__.py
│   ├── base_page.py             # Reusable UI Wrappers (click, fill, wait)
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/                       # Test Suites
│   ├── __init__.py
│   ├── conftest.py              # Global Pytest Fixtures (Setup & Teardown)
│   ├── test_ui/                 # UI-focused Test Cases
│   │   └── __init__.py
│   └── test_api/                # API-focused Test Cases
│       └── __init__.py
├── utils/                       # Shared Utility Modules
│   ├── __init__.py
│   ├── api_client.py            # API Wrapper with logging
│   └── logger.py                # System logger configuration
├── .env                         # Local Environment Credentials (Ignored in Git)
├── .gitignore                   # Files to ignore in Git
├── Dockerfile                   # Dockerization setup
├── requirements.txt             # Project Dependencies
└── README.md                    # Project Documentation