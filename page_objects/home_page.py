from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    # Locators
    LOGOUT_BUTTON = (By.ID, "btnExit")
    GREETING_TEXT = (By.ID, "textName")
    ACCOUNT_NUMBER_TEXT = (By.ID, "textAccountNumber")
    BALANCE_TEXT = (By.ID, "textBalance")
    TRANSFER_BUTTON = (By.ID, "btn-TRANSFERÊNCIA")
    PAYMENTS_BUTTON = (By.ID, "btn-PAGAMENTOS")
    STATEMENT_BUTTON = (By.ID, "btn-EXTRATO")
    WITHDRAW_BUTTON = (By.ID, "btn-SAQUE")
    BACK_BUTTON = (By.ID, "btnBack")

    def is_greeting_displayed(self):
        """Check if the greeting text is displayed on the home page."""
        return self.is_element_visible(self.GREETING_TEXT)

    def get_account_number(self):
        """Get the account number text from the home page."""
        return self.get_element_text(self.ACCOUNT_NUMBER_TEXT)

    def get_balance(self):
        """Get the account balance text from the home page."""
        return self.get_element_text(self.BALANCE_TEXT)

    def click_exit(self):
        """Click the logout button on the home page."""
        self.click_element(self.LOGOUT_BUTTON)
    
    def click_back(self):
        """Click the Back button on the home page."""
        self.click_element(self.BACK_BUTTON)