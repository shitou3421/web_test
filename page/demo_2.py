from time import sleep

from selenium.webdriver.common.by import By

from page.basepage import BasePage


class Contacts(BasePage):

    _js_add_member = (By.CSS_SELECTOR, ".js_add_member:nth-child(2)")
    _list_first = (By.XPATH, "//*[@id='member_list']")

    def get_add_text(self):
        return self.find(self._js_add_member).text

    def move_to_list(self):
        self.move_to(self._list_first)
        sleep(10)
        return self