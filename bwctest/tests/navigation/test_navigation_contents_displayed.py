import pytest
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.NavigationBar import NavigationBar


@pytest.mark.usefixtures("init_driver")
class TestContentDisplayed:
    pass