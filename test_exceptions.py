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
    @pytest.mark.third
    def test_InvalidElementStateException(self,driver):
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        #Clear input field
        driver.find_element(By.XPATH, "//button[@id='edit_btn']").click()
        #Type text into the input field
        row_1_input = driver.find_element(By.XPATH, "//div[@id='row1']//input[@class='input-field']")
        row_1_input.clear()
            # Verify the input field is empty
        assert row_1_input.get_attribute('value') == "", \
        f"Expected input field to be empty, but got '{row_1_input.get_attribute('value')}'"

    @pytest.mark.fourth
    def test_StaleElementReferenceException(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        
        # Find the instructions text element and check its content
        instruction_text = driver.find_element(By.XPATH, "//p[@id='instructions']")
        assert instruction_text.text == "Push “Add” button to add another row", \
            f"Expected instruction to display 'Push “Add” button to add another row', but got '{instruction_text.text}'"
        
        # Push add button
        driver.find_element(By.XPATH, "//button[@id='add_btn']").click()

        
        
        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver,10)
        assert wait.until(EC.invisibility_of_element_located((By.ID,"instructions")))

    @pytest.mark.fifth
    def test_TimeoutException(self,driver):
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        #Click Add button
        driver.find_element(By.XPATH, "//button[@id='add_btn']").click()
        #wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver,6)
        row_2_input_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='row2']//input[@class='input-field']")))
        #Verify second input field is displayed\
        assert row_2_input_field.is_displayed(), "Row 2 input should be displayed"