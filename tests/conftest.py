import pytest
import allure
from typing import Generator  # For type hinting of generator fixtures
from playwright.sync_api import Playwright, Browser, BrowserContext, Page
from config.settings import Settings
from utils.logger import logger

@pytest.fixture(scope="session")
def browser(playwright: Playwright) -> Generator[Browser, None, None]:
    logger.info(f"Launching browser '{Settings.BROWSER}' (Headless: {Settings.HEADLESS})")
    
    # Dynamically get the browser type from Playwright based on settings
    browser_type = getattr(playwright, Settings.BROWSER)
    
    # Launch the browser with unified settings
    browser_instance = browser_type.launch(headless=Settings.HEADLESS)
    yield browser_instance
    browser_instance.close()

@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    logger.info("Initializing Browser Context with viewport 1280x720.")
    
    # Create a new browser context with a standard viewport size for consistency across tests
    context_instance = browser.new_context(viewport={"width": 1280, "height": 720})
    yield context_instance
    context_instance.close()
    
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture a full-page screenshot on failure and 
    automatically attach it to the Allure Report.
    """
    outcome = yield
    report = outcome.get_result()
    
    # Only capture screenshot for the actual test call phase, not setup/teardown
    if report.when == "call" and report.failed:
        if "page" in item.fixturenames:
            page: Page = item.funcargs["page"]
            try:
                screenshot = page.screenshot(full_page=True)
                allure.attach(
                    screenshot,
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
                logger.error(f"Test '{item.name}' failed. Screenshot attached to Allure Report.")
            except Exception as e:
                logger.error(f"Failed to capture screenshot for failed test '{item.name}': {e}")