# pages/auth_page.py

from selenium.webdriver.common.by import By

from constants import Links
from pages.base_page import BasePage


class AuthPage(BasePage):
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "button")

    def login_ui(self, email: str, password: str) -> None:
        self.wait_until_clickable(self.EMAIL_FIELD).send_keys(email)
        self.wait_until_clickable(self.PASSWORD_FIELD).send_keys(password)
        self.wait_until_clickable(self.LOGIN_BUTTON).click()

    def check_page_is_open(self, url):
        assert self.wait_for_url_to_be(url)

    def check_profile_page_is_open(self):
        assert self.wait_for_url_to_be(self.url.replace(Links.login, Links.profile))

    def check_user_is_auth(self):
        assert self.browser.get_cookie("session")
