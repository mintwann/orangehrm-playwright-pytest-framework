from playwright.sync_api import Page
from config.settings import Settings
from utils.logger import logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = Settings.DEFAULT_TIMEOUT

    def navigate(self, url: str):
        logger.info(f"Navigating to {url}")
        self.page.goto(url)
        
    def click_element(self, selector: str, timeout: float = 10000):
        """Wait for an element to be visible and click it."""
        logger.info(f"Clicking element with selector: {selector}")
        locator = self.page.locator(selector)
        locator.wait_for(state="visible", timeout=timeout)
        locator.click()

    def fill_text(self, selector: str, text: str, timeout: float = 10000):
        """Wait for an input field and fill it with text."""
        logger.info(f"Filling text into selector: {selector}")
        locator = self.page.locator(selector)
        locator.wait_for(state="visible", timeout=timeout)
        locator.fill(text)
        
    def get_element_text(self, selector: str, timeout: float = 10000) -> str:
        """Get the text content of an element."""
        locator = self.page.locator(selector)
        locator.wait_for(state="visible", timeout=timeout)
        text = locator.text_content().strip()
        logger.debug(f"Retrieved text '{text}' from selector: {selector}")  
        return text

    def is_element_visible(self, selector: str, timeout: float = 10000) -> bool:
        """Check if an element is visible on the page."""
        try:
            self.page.locator(selector).wait_for(state="visible", timeout=timeout)
            logger.debug(f"Element with selector '{selector}' is visible.")
            return True
        except Exception:
            logger.warning(f"Element with selector '{selector}' is not visible after {timeout} ms.")
            return False
        