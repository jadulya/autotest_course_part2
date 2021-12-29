# tests\test_authorization.py
import pytest
from constants import PARAMS_FOR_NEGATIVE_AUTH, PARAMS_FOR_POSITIVE_AUTH, Links
from pages.auth_page import AuthPage
from pages.blog_pages.main_page import MainPage


@pytest.mark.auth
class TestAuthorizationClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.auth_page = AuthPage(browser, url + Links.login)
        self.auth_page.open_page()
        self.blog_page = MainPage(browser, url + Links.blog)

    @pytest.mark.smoke
    def test_login_positive(self, url):
        self.auth_page.login_ui(PARAMS_FOR_POSITIVE_AUTH["email"], PARAMS_FOR_POSITIVE_AUTH["password"])
        self.auth_page.check_page(url + Links.profile)
        self.auth_page.check_user()

    @pytest.mark.parametrize("email,password", PARAMS_FOR_NEGATIVE_AUTH, ids=["email is empty", "password is empty",
                                                                              "wrong email", "non-existent user"])
    def test_login_negative(self, email, password, url):
        self.auth_page.login_ui(email, password)
        self.auth_page.check_page(url + Links.login)

    @pytest.mark.usefixtures("login")
    def test_logout(self):
        self.blog_page.open_page()
        self.auth_page.logout()
        self.blog_page.open_page()
        self.blog_page.check_user_cannot_create_post()

