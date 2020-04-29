from page.demo_1 import Demo


class TestDemo():
    def setup(self):
        self.demo = Demo(reuse=True)

    def test_demo(self):
        content = self.demo.go_contacts().get_add_text()
        assert "添加" in content

    def test_move(self):
        self.demo.go_contacts().move_to_list()
