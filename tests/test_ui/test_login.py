from playwright.sync_api import Page
from config.settings import Settings
from pages.login_page import LoginPage

def test_valid_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login(Settings.ADMIN_USER, Settings.ADMIN_PASSWORD)
    
    page.wait_for_url("**/dashboard/index", timeout=15000)
    assert "dashboard" in page.url, f"Expected to be on the dashboard page after login, but current URL is {page.url}"
    
def test_invalid_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login("invalid_user", "invalid_pass")
    
    assert login_page.is_error_message_visible(), "Expected error message to be visible after invalid login attempt."
    error_message = login_page.get_error_message()
    assert error_message == "Invalid credentials", f"Expected error message to be 'Invalid credentials', but got '{error_message}'"