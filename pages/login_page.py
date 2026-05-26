from playwright.sync_api import Page
from config.settings import Settings
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._page_title = ".orangehrm-login-title"
        self._username_input = "input[name='username']"
        self._password_input = "input[name='password']"
        self._login_button = ".orangehrm-login-button"
        self._error_message = ".oxd-alert-content-text"

    def navigate(self) -> None:
        super().navigate(Settings.BASE_URL)

    def login(self, username: str, password: str) -> None:
        self.fill_text(self._username_input, username)
        self.fill_text(self._password_input, password)
        self.click(self._login_button)
    
    def get_page_title(self) -> str:
        return self.get_element_text(self._page_title)
        
    def get_error_message(self) -> str:
        if self.is_element_visible(self._error_message):
            return self.get_element_text(self._error_message)
        return ""
    
    def is_error_message_visible(self) -> bool:
        return self.is_element_visible(self._error_message)