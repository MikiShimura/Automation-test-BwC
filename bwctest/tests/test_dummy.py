import pytest

@pytest.mark.usefixtures("init_driver")
class TestDummy():

    @pytest.mark.dummy
    def test_dummy_func(self):
        print("I am dummy test line1")
        print("I am dummy test line2")
        self.driver.get("https://www.google.co.jp/")
        import pdb; pdb.set_trace()