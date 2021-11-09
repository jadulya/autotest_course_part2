import pytest
from constants import PARAMS_FOR_NEGATIVE_AUTH
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import wait_until_clickable, wait_until_url_to_be, login


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self):
        with Chrome() as browser:
            browser.get('https://qastand.valhalla.pw/login')
            browser.maximize_window()
            login(browser)
            assert browser.get_cookie("session"), "Вы не авторизовались"

    @pytest.mark.parametrize("email,password", PARAMS_FOR_NEGATIVE_AUTH, ids=["email is empty", "password is empty",
                                                                              "wrong email", "non-existent user"])
    def test_login_negative(self, email, password):
        with Chrome() as browser:
            browser.get('https://qastand.valhalla.pw/login')
            browser.maximize_window()
            wait_until_clickable(browser, (By.NAME, 'email')).send_keys(email)
            wait_until_clickable(browser, (By.NAME, 'password')).send_keys(password)
            wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
            wait_until_url_to_be(browser, 'https://qastand.valhalla.pw/login'), "Вы смогли авторизоватьяся"
