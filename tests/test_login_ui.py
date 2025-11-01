import pytest
from assertpy import assert_that
from playwright.sync_api import sync_playwright

from base.automation_wrapper import AutomationWrapper


class TestLoginUI(AutomationWrapper):

    def test_title(self):
        assert_that("OpenEMR Login").is_equal_to(self.page.title())

    def test_placeholder(self):
        actual_username_placeholder=self.page.locator("css=#authUser").get_attribute("placeholder")
        actual_password_placeholder = self.page.locator("css=#clearPass").get_attribute("placeholder")

        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").contains(actual_password_placeholder)


