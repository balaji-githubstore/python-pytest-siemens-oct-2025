import pytest
from playwright.sync_api import sync_playwright


class AutomationWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        playwright_manager = sync_playwright()
        playwright = playwright_manager.start()
        browser = playwright.chromium.launch(headless=False, channel="chrome",
                                             executable_path=r"D:\Balaji\Components\chrome-win64\chrome-win64\chrome.exe")
        context = browser.new_context()
        self.page = context.new_page()
        self.page.goto("https://demo.openemr.io/b/openemr")
        yield
        playwright.stop()