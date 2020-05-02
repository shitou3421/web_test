import os

import allure
from selenium.webdriver.remote.webdriver import WebDriver


def attach(driver: WebDriver, name):
    '''
    截图并保存到allure报告上
    '''
    temp_name = "xx.png"
    name = "步骤" + repr(name) # 强制转换为字符串
    driver.get_screenshot_as_file(temp_name)
    allure.attach.file(temp_name, attachment_type=allure.attachment_type.PNG, name=name)
    os.remove(temp_name)


class AttachVideo():
    '''
    实现运行录屏的方法， web端暂不需要实现，在移动端实现
    '''
    pass


class Mysql():
    '''
    mysql相关的操作
    '''

    def connect(self):
        pass

    def disconnect(self):
        pass

    def read(self):
        pass

    def insert(self):
        pass


class Redis():
    '''
    redis相关的操作
    '''
    def connect(self):
        pass

    def disconnect(self):
        pass

    def read(self):
        pass

    def insert(self):
        pass
