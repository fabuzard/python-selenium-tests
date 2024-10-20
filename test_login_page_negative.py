import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type incorrect username
        driver.find_element(By.ID, "username").send_keys("incorrectUser")
        # Type password
        driver.find_element(By.ID, "password").send_keys("Password123")
        # Submit
        driver.find_element(By.XPATH, "//button[@class='btn']").click()

        # Verify error message
        error_locator = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        assert (
            error_locator.is_displayed()
        ), "Error message is not displayed, but it should be."
        assert (
            error_locator.text == "Your username is invalid!"
        ), "Unexpected error message."

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type correct username
        driver.find_element(By.ID, "username").send_keys("student")
        # Type incorrect password
        driver.find_element(By.ID, "password").send_keys("incorrectpassword")
        # Submit
        driver.find_element(By.XPATH, "//button[@class='btn']").click()

        # Verify error message
        error_locator = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        assert (
            error_locator.is_displayed()
        ), "Error message is not displayed, but it should be."
        assert (
            error_locator.text == "Your password is invalid!"
        ), "Unexpected error message."

    @pytest.mark.negativeP
    @pytest.mark.parametrize(
        "username, password, expected_error_message",
        [
            ("incorrectUser", "Password123", "Your username is invalid!"),
            ("student", "incorrectpassword", "Your password is invalid!"),
        ],
    )
    def test_negative_login(self, driver, username,password, expected_error_message):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type correct username
        driver.find_element(By.ID, "username").send_keys(username)
        # Type incorrect password
        driver.find_element(By.ID, "password").send_keys(password)
        # Submit
        driver.find_element(By.XPATH, "//button[@class='btn']").click()

        # Verify error message
        error_locator = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        assert (
            error_locator.is_displayed()
        ), "Error message is not displayed, but it should be."
        assert (
            error_locator.text == expected_error_message
        ), "Unexpected error message."
