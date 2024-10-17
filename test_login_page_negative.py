from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
import time
import pytest

class TestNegativeScenarios:   
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self): 
        driver = webdriver.Edge()
 
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        #Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID,"username").send_keys("incorrectUser")
        #Type password Password123 into Password field
        password_locator = driver.find_element(By.ID,"password").send_keys("Password123")
        #Push Submit button
        submit_button_locator = driver.find_element(By.XPATH,"//button[@class='btn']").click()
        #Verify error message is displayed
        time.sleep(1)
        error_locator = driver.find_element(By.ID,"error")
        assert error_locator.is_displayed(), "Error message is not displayed, but it should be displayed"
        #Verify error message text is Your username is invalid!
        assert error_locator.text == "Your username is invalid!", "Error message is not expected"
        time.sleep(5)
