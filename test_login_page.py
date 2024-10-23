
from selenium.webdriver.common.by import By
import time
import pytest


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self,driver):
       
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")



        #Type username student into Username field
        username_locator = driver.find_element(By.ID,"username").send_keys("student")

        #Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME,"password").send_keys("Password123")

        #Push Submit button
        submit_button_locator = driver.find_element(By.XPATH,"//button[@class='btn']").click()

        #Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url=driver.current_url

        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"


        #Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME,"h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        #Verify button Log out is displayed on the new page
        logout_locator = driver.find_element(By.LINK_TEXT,"Log out")
        assert logout_locator.is_displayed()
        time.sleep(2)
        logout_locator.click()

        time.sleep(5)