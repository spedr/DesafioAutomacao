from time import sleep
from selenium.webdriver.common.by import By
from .base_page import BasePage
from config import BROWSER_LOCALE

class TransferPage(BasePage):
    # Locators
    ACCOUNT_NUMBER_INPUT = (By.NAME, "accountNumber")
    ACCOUNT_DIGIT_INPUT = (By.NAME, "digit")
    TRANSFER_VALUE_INPUT = (By.NAME, "transferValue")
    DESCRIPTION_INPUT = (By.NAME, "description")
    TRANSFER_BUTTON = (By.XPATH, "//button[contains(text(),'Transferir agora')]")
    SUCCESS_MODAL_TEXT = (By.ID, "modalText")
    ERROR_MODAL_TEXT = (By.ID, "modalText")
    CLOSE_MODAL_BUTTON = (By.ID, "btnCloseModal")


    def fill_account_number(self, account_number):
        """Fill in the account number."""
        self.type_into_element(self.ACCOUNT_NUMBER_INPUT, account_number)

    def fill_account_digit(self, digit):
        """Fill in the account digit."""
        self.type_into_element(self.ACCOUNT_DIGIT_INPUT, digit)

    def fill_transfer_value(self, value):
        """Fill in the transfer value, formatting according to the browser locale."""
        # formatted_value = self.format_value_according_to_locale(value)
        formatted_value = self.format_value(value)
        self.type_into_element(self.TRANSFER_VALUE_INPUT, formatted_value)

    def fill_description(self, description):
        """Fill in the transfer description."""
        self.type_into_element(self.DESCRIPTION_INPUT, description)

    def submit_transfer(self):
        """Click the 'Transferir agora' button to submit the transfer form."""

        # It seems that for whatever mystical e2e reason, we need to double click this button.
        # self.click_element(self.TRANSFER_BUTTON)
        self.double_click_element(self.TRANSFER_BUTTON)

    def is_transfer_successful(self):
        """Check if the transfer success message is displayed."""
        success_message = self.get_element_text(self.SUCCESS_MODAL_TEXT)
        return "Transferencia realizada com sucesso" in success_message

    def is_insufficient_funds_error_displayed(self):
            """Check if the error message for insufficient funds is displayed."""
            error_message = self.get_element_text(self.ERROR_MODAL_TEXT)
            return "Você não tem saldo suficiente para essa transação" in error_message

    def close_modal(self):
        """Close the transfer modal."""
        self.click_element(self.CLOSE_MODAL_BUTTON)

    def format_value_according_to_locale(self, value):
        """Format the given value as a string according to the browser locale."""
        # It seems that this function was useless after all, given BugBank won't
        # accept values like R$ 1000,00 even on pt-BR locale.
        # Still, I will keep it here for future use.

        # value_str = f"{value:.2f}" # Normally having this code here would be more consistent
                                     # but since we will stress a couple errors, we'll leave it out.
        value_str = str(value)
        if BROWSER_LOCALE == "pt-BR":
            return value_str.replace(".", ",")  # For Brazilian Portuguese, replace dot with comma
        else:
            # Default formatting for "en-US" follows the Python standard
            return value_str.replace(",", ".")
    
    def format_value(self, value):
        """Format the given value to a . (dot) separated value that BugBank will accept."""
        return str(value).replace(",", ".")