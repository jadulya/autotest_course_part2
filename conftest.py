import pytest
from selenium.webdriver import Chrome


@pytest.fixture()
def browser():
    browser = Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: tests for smoke testing"
    )
    config.addinivalue_line(
        "markers", "auth: test for authorization"
    )
