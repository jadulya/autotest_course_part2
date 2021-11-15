import time

from selenium.webdriver.common.by import By
from constants import Links
from functions import wait_until_clickable, wait_until_visible


class TestBlogClass:
    def test_open_post(self, browser):
        browser.get(Links.post_user2)
        wait_until_clickable(browser, (By.CSS_SELECTOR, '[href="/blog/page/1/test-post/"]')).click()
        text = wait_until_visible(browser, (By.CSS_SELECTOR, 'p:nth-child(5)')).text
        assert text == 'Hello world!', 'Неверный текст'
