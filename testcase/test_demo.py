import allure
import pytest

from page.demo_1 import Demo


class TestDemo():
    def setup(self):
        self.demo = Demo(reuse=True)

    @pytest.mark.parametrize("text", [
        "添加", "四川", "成功", "成员"
    ])
    def test_demo(self, text):
        content = self.demo.go_contacts().get_add_text()
        assert text in content

    def test_move(self):
        self.demo.go_contacts().move_to_list()
