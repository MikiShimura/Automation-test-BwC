import pytest
from src.pages.LoginPage import LoginPage
from src.pages.RegisterPage import RegisterPage
from src.pages.HomePage import HomePage
from src.pages.SiteDetailedPage import SiteDetailedPage
from src.pages.Alert import Alert
from src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
class TestEditDeleteSitesPositive:
    pass