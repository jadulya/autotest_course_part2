import pytest
from constants import Links, SESSION_COOKIE


@pytest.fixture(autouse=True)
def login(browser):
    browser.get(Links.base_url)
    browser.add_cookie(SESSION_COOKIE)
