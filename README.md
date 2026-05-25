# OrangeHRM Hybrid Test Automation Framework

A professional-grade Hybrid Test Automation Framework designed for the OrangeHRM (Open Source v5.x) web application. This project demonstrates modern automation engineering practices, combining UI and API testing to achieve fast, robust, and scalable test execution.


## Key Features

- **Hybrid Testing Approach**: Speeds up execution by using API requests for test data setup (pre-requisites) and teardown (cleanup), reserving UI automation solely for high-value user scenarios.
- **Page Object Model (POM)**: Implemented using custom wrappers over Playwright for highly maintainable and readable UI actions.
- **Robust API Client**: A lightweight wrapper around Python's `requests` library with integrated logging and error handling.
- **Centralized Logging System**: Implements Python's native `logging` module to output standardized log formats to both the Console and timestamped log files under `/logs/`, categorized by levels (`INFO`, `DEBUG`, `WARNING`, `ERROR`).
- **Configuration Management**: Centralized environment configuration using `.env` and `config.ini` files to ensure seamless switching between Dev, Staging, and Production environments.
- **Rich Reporting**: Integrated with Allure Report to generate interactive HTML reports, automatically capturing screenshots and logs upon failure.
- **CI/CD Pipeline**: GitHub Actions workflow that automatically executes tests in headless browsers and deploys Allure Reports directly to GitHub Pages.
- **Dockerized Execution**: Dockerfile configuration allowing tests to run in an isolated and consistent environment.


## Tech Stack

- **Language**: Python 3.11+ (Fully compatible with Python 3.13)
- **Test Runner**: Pytest
- **UI Engine**: Playwright (with `pytest-playwright` plugin)
- **API Engine**: Requests
- **Reporting**: Allure Report
- **CI/CD**: GitHub Actions & GitHub Pages
- **Containerization**: Docker


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
├── logs/                        # Automatically generated log files
├── pages/                       # UI Page Object Classes
│   ├── __init__.py
│   ├── base_page.py             # Reusable UI Wrappers with integrated logging
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/                       # Test Suites
│   ├── __init__.py
│   ├── conftest.py              # Global Pytest Fixtures (Setup, Teardown & Screenshot hook)
│   ├── test_ui/                 # UI-focused Test Cases
│   │   ├── __init__.py
│   │   └── test_login.py
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
```


## Getting Started

### Prerequisites
- **Python 3.11 - 3.13** installed on your machine.
- **Git** installed.
- **Allure Commandline** installed (Required to generate and view the HTML reports locally).
  - *Windows (via Scoop):* `scoop install allure`
  - *Windows (via Chocolatey):* `choco install allure`
  - *macOS (via Homebrew):* `brew install allure`

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/orangehrm-playwright-pytest-framework.git
   cd orangehrm-playwright-pytest-framework
   ```

2. **Set up the Virtual Environment:**
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies & Playwright Browsers:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

4. **Environment Configuration:**
   Create a `.env` file in the root directory and define the target environment variables:
   ```env
   BASE_URL = your-url
   ADMIN_USER = your-username
   ADMIN_PASSWORD = your-password
   ```

##  Running Tests

To run the test suite locally, use the following commands:

### 1. Basic Execution
Run all tests:
  ```bash
  pytest -v
  ```

### 2. Execution with Real-Time Console Logs
Our custom formatted logs are natively captured and displayed directly in your terminal in real-time (managed by the pytest.ini configuration):
```bash
pytest -v tests/test_ui/test_login.py
```

### 3. Execution with Allure Report Generation
To execute tests and output metadata for Allure Report:
```bash
# Run tests and collect data into 'allure-results' folder
pytest -v --alluredir=allure-results

# Generate and open the interactive HTML report in your browser
allure serve allure-results
```


## Verifying Logs and Artifacts

After executing the tests, check the following generated folders on your local machine:
1. **`/logs/`**: Contains execution log files (e.g., `execution_YYYY-MM-DD.log`).
2. **`/allure-results/`**: Contains JSON/XML metadata for report generation.
3. **`failure_screenshot` (Embedded in Allure)**: If a test fails, a full-page screenshot is automatically generated and embedded into the Allure report under the failed test case details.