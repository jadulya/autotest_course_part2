import pytest
from constants import PARAMS_FOR_NEGATIVE_AUTH, PARAMS_FOR_POSITIVE_AUTH, Links
from functions import wait_until_url_to_be, login_ui


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self, browser):
        browser.get(Links.login)
        login_ui(browser, PARAMS_FOR_POSITIVE_AUTH['email'], PARAMS_FOR_POSITIVE_AUTH['password'])
        assert browser.get_cookie("session"), "Вы не авторизовались"

    @pytest.mark.parametrize("email,password", PARAMS_FOR_NEGATIVE_AUTH, ids=["email is empty", "password is empty",
                                                                              "wrong email", "non-existent user"])
    def test_login_negative(self, email, password, browser):
        browser.get(Links.login)
        login_ui(browser, email, password)
        wait_until_url_to_be(browser, Links.login), "Вы смогли авторизоваться"
