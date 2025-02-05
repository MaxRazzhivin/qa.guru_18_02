import pytest
from selene import browser

@pytest.fixture(scope="session")
def setting_browser():
    browser.config.window_height = 800
    browser.config.window_width = 600



@pytest.fixture()
def open_browser(setting_browser):
    browser.open('https://google.com')
    yield
    browser.quit()

@pytest.fixture()
def open_duckgo(setting_browser):
    browser.open('https://duckduckgo.com/')
    yield
    browser.quit()
