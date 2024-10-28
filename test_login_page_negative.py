import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page_objects.base_page import BasePage
from page_objects.login_page import LoginPage


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_username(self, driver,username,password,expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username,password)
        assert login_page.get_error_message() == expected_error_message, "the error message is not as expected"


    
