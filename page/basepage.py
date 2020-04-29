import os
import logging

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BasePage():

    _url = ""

    def __init__(self, driver: WebDriver = None, reuse=False):
        # 浏览器的重用， 多浏览器的支持，
        browser = os.getenv("browser", "")
        if browser == "firefox":
            self._driver = webdriver.Firefox()
        elif browser == "ie":
            self._driver = webdriver.Ie()
        elif browser == "headless":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1280,1686")
            self._driver = webdriver.Chrome(options=options)
        else:  # 默认使用chrome浏览器
            if driver is None:
                if reuse:
                    options = webdriver.ChromeOptions()
                    options.debugger_address = "127.0.0.1:9999"  # 使用已打开的浏览器进行调试
                    self._driver = webdriver.Chrome(options=options)
                else:
                    self._driver = webdriver.Chrome()
            else:
                self._driver = driver
        logger.info("初始化浏览器， 当前使用的浏览器为{browser}".format(browser=browser))
        self._driver.maximize_window()
        self._driver.implicitly_wait(5)
        if self._url != "":
            self._driver.get(self._url)

    def __wait(self, locator:tuple):
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def find(self, locator, value=None, group=False):
        logger.info("当前查找元素为：{locator}, {value}".format(locator=locator, value=value))
        if group:
            if isinstance(locator, tuple):
                self.__wait(locator)
                return self._driver.find_elements(*locator)
            else:
                self.__wait((locator, value))
                return self._driver.find_elements(locator, value)
        else:
            if isinstance(locator, tuple):
                self.__wait(locator)
                return self._driver.find_element(*locator)
            else:
                self.__wait((locator, value))
                return self._driver.find_element(locator, value)

    def close(self):
        self._driver.close()

    def move_to(self, locator:tuple): # 某些元素需要将鼠标移动到特定元素才能显现操作
        logger.info("移动鼠标至：{locator}".format(locator=locator))
        element = self.find(locator)
        ActionChains(self._driver).move_to_element(element).perform()


