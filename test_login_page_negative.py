from selenium import webdriver
from selenium.webdriver.edge.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def driver():
    print("Creating Edge driver")
    my_driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    yield my_driver
    print("Closing Edge driver")
    my_driver.quit()

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
        assert error_locator.is_displayed(), "Error message is not displayed, but it should be."
        assert error_locator.text == "Your username is invalid!", "Unexpected error message."

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
        assert error_locator.is_displayed(), "Error message is not displayed, but it should be."
        assert error_locator.text == "Your password is invalid!", "Unexpected error message."
