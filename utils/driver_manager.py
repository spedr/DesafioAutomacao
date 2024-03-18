from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import json
from config import BROWSER_HEADLESS, BROWSER_TYPE, BROWSER_LOCALE

class DriverManager:
    @staticmethod
    def get_driver():
        if BROWSER_TYPE == "chrome":
            return DriverManager.get_chrome_driver()
        elif BROWSER_TYPE == "firefox":
            return DriverManager.get_firefox_driver()
        else:
            raise ValueError(f"Unsupported browser type: {BROWSER_TYPE}")

    @staticmethod
    def get_chrome_driver():
        options = webdriver.ChromeOptions()
        if BROWSER_HEADLESS:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f'--lang={BROWSER_LOCALE}')
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    @staticmethod
    def get_firefox_driver():
        options = webdriver.FirefoxOptions()
        if BROWSER_HEADLESS:
            options.add_argument('--headless')
        options.set_preference("intl.accept_languages", BROWSER_LOCALE)
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)
    
    @staticmethod
    def set_local_storage(driver, data_path='utils/accounts.json'):
        with open(data_path, 'r') as file:
            accounts_data = json.load(file)
        
        for email, account_info in accounts_data.items():
            account_info_str = json.dumps(account_info)
            driver.execute_script(f"window.localStorage.setItem('{email}', {json.dumps(account_info_str)});")
