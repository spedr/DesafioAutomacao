import subprocess
import os
import datetime
import webbrowser
from config import JUNIT_RESULTS_PATH, HTML_REPORTS_PATH, AUTO_OPEN_REPORT

def generate_junit_html_report():
    """
    Generate a JUnit HTML report from report files in the JUNIT_RESULTS_PATH.
    If more than one report file is found, they are merged into a single report before generating the HTML.
    """

    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    report_files = [f for f in os.listdir(JUNIT_RESULTS_PATH) if f.endswith('.xml')]
    report_files_full_path = [os.path.join(JUNIT_RESULTS_PATH, f) for f in report_files]
    output_html = os.path.join(HTML_REPORTS_PATH, f"junit_report_{current_datetime}.html")

    if len(report_files_full_path) > 1:
        subprocess.run(['junit2html', '--merge', *report_files_full_path])
        merged_xml = report_files_full_path[0]
        command = ['junit2html', merged_xml, output_html]
    elif report_files_full_path:
        command = ['junit2html'] + report_files_full_path + [output_html]
    else:
        print("No report files found in the specified folder.")
        return

    subprocess.run(command)
    print(f"JUnit HTML report generated: {output_html}")

    if AUTO_OPEN_REPORT:
        webbrowser.open('file://' + os.path.realpath(output_html))
        print(f"JUnit HTML report opened in browser: {output_html}")

if __name__ == "__main__":
    os.makedirs(HTML_REPORTS_PATH, exist_ok=True)
    generate_junit_html_report()