from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Acessar')]")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Registrar')]")
    MODAL_TEXT = (By.ID, "modalText")
    CLOSE_MODAL_BUTTON = (By.ID, "btnCloseModal")


    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        """Enter the email in the email input field."""
        self.type_into_element(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Enter the password in the password input field."""
        self.type_into_element(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the login button."""
        self.click_element(self.LOGIN_BUTTON)

    def click_register(self):
        """Click the register button."""
        self.click_element(self.REGISTER_BUTTON)

    def login(self, email, password):
        """Convenience function to log in."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_login_failure_modal_displayed(self):
        """Check if the login failure modal is displayed."""
        return self.is_element_visible(self.MODAL_TEXT)

    def get_login_failure_message(self):
        """Retrieve the login failure message from the modal."""
        return self.get_element_text(self.MODAL_TEXT)

    def close_login_failure_modal(self):
        """Close the login failure modal."""
        self.click_element(self.CLOSE_MODAL_BUTTON)