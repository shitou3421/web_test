
from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.demo_2 import Contacts


class Demo(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _contacts = (By.CSS_SELECTOR, "#menu_contacts")

    def go_contacts(self):
        self.find(self._contacts).click()
        return Contacts(driver=self._driver)

