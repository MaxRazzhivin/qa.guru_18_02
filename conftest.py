import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def setting_browser():
    browser.driver.maximize_window()
    yield
    browser.quit()


@pytest.fixture()
def open_google():
    browser.open('https://google.com')


@pytest.fixture()
def open_duckgo():
    browser.open('https://duckduckgo.com/')


@pytest.fixture()
def open_niffler():
    browser.open('https://niffler.qa.guru')
    yield
    browser.quit()
