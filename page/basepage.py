import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.utils import *

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class BasePage():

    _url = ""

    def __init__(self, driver: WebDriver = None, reuse=False, remote=False):
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
                    # options.debugger_address = "127.0.0.1:9999"  # 使用已打开的浏览器进行调试
                    if remote:
                        self._driver = webdriver.Remote(
                            command_executor="http://10.1.1.248:4444/wd/hub",
                            desired_capabilities=DesiredCapabilities.CHROME,
                            options=options,
                        )
                    self._driver = webdriver.Chrome(options=options)
                else:
                    self._driver = webdriver.Chrome()
            else:
                self._driver = driver
        self._driver.maximize_window()
        self._driver.implicitly_wait(5)
        if self._url != "":
            self._driver.get(self._url)
        try:
            self.setcookies()
            sleep(3)
        except Exception as e:
            pass
        finally:
            self._driver.refresh()

    def __wait(self, locator:tuple):
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        attach(self._driver, name=locator)  # 做到每一步都截图记录到allure报告上

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

    def getcookies(self):
        cookies = self._driver.get_cookies()
        with open("cookies.txt", "w+") as f:
            for cookie in cookies:
                print(cookie)
                cookie = str(cookie)
                f.write(cookie + "\n")

    def setcookies(self):
        with open("cookies.txt", "r+") as f:
            for line in f:
                cookie = eval(line.strip())
                print(cookie)
                self._driver.add_cookie(cookie)
