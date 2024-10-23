from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class TestExceptions:
    @pytest.mark.exceptions
    @pytest.mark.first
    def test_NoSuchElementException(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        driver.find_element(By.XPATH, "//button[@id='add_btn']").click()

        wait = WebDriverWait(driver, 10)
        # Verify Row 2 input field is displayed
        row_2_input_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']")))
        
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed"
        # Row 2 doesn’t appear immediately. This test will fail with org.openqa.selenium.NoSuchElementException without proper wait

    @pytest.mark.exceptions
    @pytest.mark.second
    def test_ElementNotInteractableException(self, driver):
            # Open page
            driver.get("https://practicetestautomation.com/practice-test-exceptions/")
            
            # Click Add button and wait for Row 2 to load
            driver.find_element(By.XPATH, "//button[@id='add_btn']").click()
            wait = WebDriverWait(driver, 10)
            
            # Wait for the second row to become clickable (ready for interaction)
            row_2_input_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='row2']//input[@class='input-field']")))
            # Type text into the second input field
            row_2_input_field.send_keys("Genburgir")
            
            # Wait for Save button to be clickable and click it
            save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='row2']//button[@id='save_btn']")))
            save_button.click()
            
            # Verify confirmation text is displayed
            saved_text = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='confirmation']")))
            assert saved_text.is_displayed(), "The confirmation text should be displayed"