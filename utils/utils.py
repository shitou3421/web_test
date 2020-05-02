import os

import allure
import pymysql
from selenium.webdriver.remote.webdriver import WebDriver


def attach(driver: WebDriver, name):
    '''
    截图并保存到allure报告上
    '''
    temp_name = "xx.png"
    name = "步骤" + repr(name)  # 强制转换为字符串
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
    mysql的连接
    ip = "127.0.0.1"
    username = "root"
    password = "mysql"
    db = "test_db"
    db = Mysql().connect(ip, username, password, db)
    db.execute("create table test_one (`id` int auto_increment not null primary key, `name` varchar(30) not null);")
    '''

    def connect(self, ip, username, password, db):
        self.cursor = pymysql.connect(ip, username, password, db).cursor()
        return self.cursor

    def preset_data(self):
        '''
        前置准备数据
        :return:
        '''
        pass

    def post_data(self):
        '''
        后置清理数据
        :return:
        '''
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

    def delete(self):
        pass

# if __name__ == '__main__':
#     ip = "127.0.0.1"
#     username = "root"
#     password = "mysql"
#     db = "test_db"
#     db = Mysql().connect(ip, username, password, db)
#     db.execute("create table test_one (`id` int auto_increment not null primary key, `name` varchar(30) not null);")
#     db.close()
