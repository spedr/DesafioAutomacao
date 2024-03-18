from behave import use_step_matcher, step
from utils.driver_manager import DriverManager
from utils.capture_stdout import CaptureStdout
from utils.sanitize_filename import sanitize_filename
from config import REPORT_ENGINE
import allure
import datetime
import os

def before_all(context):
    context.driver = DriverManager.get_driver()

def before_scenario(context, scenario):
    # Preload local storage with account data before each scenario
    context.driver.get("https://bugbank.netlify.app")
    DriverManager.set_local_storage(context.driver)

def after_all(context):
    # Clean up
    if hasattr(context, 'driver'):
        context.driver.quit()

def before_step(context, step):
    if REPORT_ENGINE == 'allure':
        context.stdout_capture = CaptureStdout()
        context.stdout_capture.__enter__()

def after_step(context, step):
    if REPORT_ENGINE == 'allure':
        context.stdout_capture.__exit__()
        captured_output = context.stdout_capture.captured
        if captured_output:
            allure.attach(captured_output, name=f"Step Output: {step.name}", attachment_type=allure.attachment_type.TEXT)

        if step.status == "failed":
            screenshot_directory = "screenshots"
            if not os.path.exists(screenshot_directory):
                os.makedirs(screenshot_directory)
            
            sanitized_step_name = sanitize_filename(step.name)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_file_path = f"{screenshot_directory}/screenshot_{sanitized_step_name}_{timestamp}.png"
            context.driver.save_screenshot(screenshot_file_path)
            
            # Attach the screenshot to the Allure report
            with open(screenshot_file_path, "rb") as file:
                file_content = file.read()
                allure.attach(file_content, name=f"Screenshot: {sanitized_step_name}", attachment_type=allure.attachment_type.PNG)

