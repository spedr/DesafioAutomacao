from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

try:
    from config import DEFAULT_TIMEOUT, VERBOSE
except ImportError:
    DEFAULT_TIMEOUT = 10  # Fallback default timeout
    VERBOSE = False

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _log(self, message):
        """Helper function to log messages based on verbosity setting."""
        if VERBOSE:
            print(message)

    def navigate_to(self, url):
        """Navigate to a specified URL."""
        self._log(f"Navigating to URL: {url}")
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for an element to be visible and return it."""
        self._log(f"Waiting for element with locator: {locator}, timeout: {timeout} seconds")
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        self._log(f"Element found and is visible: {locator}")
        return element

    def find_element(self, locator):
        """Find and return an element by its locator."""
        self._log(f"Attempting to find element with locator: {locator}")
        try:
            element = self.driver.find_element(*locator)
            self._log(f"Element found: {locator}")
            return element
        except NoSuchElementException:
            self._log(f"Element not found: {locator}")
            return None

    def is_element_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        """Check if an element is visible."""
        self._log(f"Checking visibility for element with locator: {locator}, timeout: {timeout} seconds")
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            self._log(f"Element is visible: {locator}")
            return True
        except TimeoutException:
            self._log(f"Element not visible within timeout: {locator}")
            return False

    def click_element(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for an element to be clickable and click it."""
        self._log(f"Waiting for element to be clickable with locator: {locator}, timeout: {timeout} seconds")
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
        self._log(f"Clicked element with locator: {locator}")

    def javascript_click(self, locator, timeout=DEFAULT_TIMEOUT):
        """Use JavaScript to click the 'Transferir agora' button if regular click doesn't work."""
        # Originally written as a workaround for the transfer button problem.
        # Kept in the codebase just in case it's useful one day.
        self._log(f"Waiting for element to be clickable with locator: {locator}, timeout: {timeout} seconds")
        button = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", button)
    
    def double_click_element(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for an element to be clickable and double-click it."""
        self._log(f"Waiting for element to be clickable with locator: {locator}, timeout: {timeout} seconds")
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(element).double_click().perform()
        self._log(f"Double-clicked element with locator: {locator}")

    def type_into_element(self, locator, text, timeout=DEFAULT_TIMEOUT):
        """Type text into an input field."""
        self._log(f"Typing text into element. Locator: {locator}, Text: '{text}', Timeout: {timeout} seconds")
        element = self.wait_for_element(locator, timeout)
        element.clear()
        self._log("Existing text cleared")
        element.send_keys(text)
        self._log(f"Text '{text}' typed into element: {locator}")

    def get_element_text(self, locator, timeout=DEFAULT_TIMEOUT):
        """Get text from an element."""
        self._log(f"Getting text from element with locator: {locator}, timeout: {timeout} seconds")
        element = self.wait_for_element(locator, timeout)
        text = element.text
        self._log(f"Text retrieved from element {locator}: '{text}'")
        return text
