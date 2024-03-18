import subprocess
import os
from config import REPORT_ENGINE, JUNIT_RESULTS_PATH, AUTO_OPEN_REPORT
from .junit_html_report import generate_junit_html_report

def run_behave_tests(features):
    """
    Run Behave tests for the specified list of feature files and generate reports.
    """
    allure_results_path = './allure-results'
    allure_report_path = './allure-report'

    for feature in features:
        if REPORT_ENGINE == 'allure':
            os.makedirs(allure_results_path, exist_ok=True)
            subprocess.run(['behave', '-f', 'allure_behave.formatter:AllureFormatter', '-o', allure_results_path, feature])
            print("Allure report generated for: " + feature)
        
        elif REPORT_ENGINE == 'junit':
            subprocess.run(['behave', '--junit', '--junit-directory', JUNIT_RESULTS_PATH, feature])
            print("JUnit XML report generated for: " + feature)
    
    if REPORT_ENGINE == 'allure':
        # Test history set up
        history_dir = os.path.join(allure_report_path, 'history')
        if os.path.isdir(history_dir):
            os.makedirs(os.path.join(allure_results_path, 'history'), exist_ok=True)
            for file in os.listdir(history_dir):
                os.replace(os.path.join(history_dir, file), os.path.join(allure_results_path, 'history', file))
        
        subprocess.run('allure generate {} -o {} --clean'.format(allure_results_path, allure_report_path), shell=True)

        print(f"Allure report generated at {allure_report_path}")
        
        if AUTO_OPEN_REPORT:
            subprocess.run(f'allure open {allure_report_path}', shell=True)
            print(f"Allure report opened in browser: {allure_report_path}")
    elif REPORT_ENGINE == 'junit':
        print("Generating HTML report from JUnit XML reports...")
        generate_junit_html_report()
    elif REPORT_ENGINE != 'allure':
        print(f"Unsupported report engine: {REPORT_ENGINE}")
