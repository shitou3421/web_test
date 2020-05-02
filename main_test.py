import os
import shutil


def run(allure_tmp, junit_path, allure_html, case_path, report_path):
    shutil.rmtree(report_path)  # 删除带有文件的文件夹
    os.system(f"pytest --alluredir={allure_tmp} --junitxml={junit_path} {case_path}")
    os.system(f"allure generate {allure_tmp} -o {allure_html}")


if __name__ == '__main__':
    project_root = os.path.abspath(os.path.dirname(__file__))
    case_path = os.path.join(project_root, "testcase")
    report_path = os.path.join(project_root, "report")
    allure_tmp = os.path.join(project_root, "report", "allure_tmp")
    junit_path = os.path.join(project_root, "report", "junit_path", "junit.xml")
    allure_html = os.path.join(project_root, "report", "allure_html")

    run(allure_tmp, junit_path, allure_html, case_path, report_path)
