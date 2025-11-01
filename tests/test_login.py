import pytest
from assertpy import assert_that

from base.automation_wrapper import AutomationWrapper
from pages.login_page import LoginPage
from utilities.data_source import DataSource


class TestLogin(AutomationWrapper):

    @pytest.mark.parametrize("username,password,expected_title",
                             DataSource.valid_login_data_excel)
    def test_valid_login(self,username,password,expected_title):
        self.page.locator("css=#authUser").fill(username)
        self.page.locator("css=#clearPass").fill(password)
        self.page.locator("css=#login-button").click()
        assert_that(expected_title).is_equal_to(self.page.title())


