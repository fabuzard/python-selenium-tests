from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:
    @pytest.mark.exceptions
    @pytest.mark.first
    def test_NoSuchElementException(self, driver):
        # Open page
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        # Click Add button
        # Verify Row 2 input field is displayed
        exceptions_page.add_second_row()
        
        assert exceptions_page.is_row2_isdisplayed(), "Row 2 should be displayed"
        # Row 2 doesn’t appear immediately. This test will fail with org.openqa.selenium.NoSuchElementException without proper wait

    @pytest.mark.exceptions
    @pytest.mark.second
    def test_ElementNotInteractableException(self, driver):
            # Open page
            exceptions_page = ExceptionsPage(driver)
            exceptions_page.open()
            # Click Add button and wait for Row 2 to load
            exceptions_page.add_second_row()
            
            # Wait for the second row to become clickable (ready for interaction)
            

            # Type text into the second input field

            # Wait for Save button to be clickable and click it
            # Verify confirmation text is displayed
            exceptions_page.row2_input_element("Genburgir")       
            assert exceptions_page.get_confirmation_message()=="Row 2 was saved", "The confirmation text should be displayed"
    @pytest.mark.third
    def test_InvalidElementStateException(self,driver):
        # Open page
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        #Clear input field
        exceptions_page.modify_row1_input("Genburgir")
        assert exceptions_page.get_confirmation_message()=="Row 1 was saved", "The confirmation text should be displayed"

    @pytest.mark.fourth
    def test_StaleElementReferenceException(self, driver):
        # Open page
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()

        assert not exceptions_page.are_instruction_displayed(),"Instruction text element should not be displayed"

    @pytest.mark.fifth
    def test_TimeoutException(self,driver):
        #Open page
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        #Click Add button
        exceptions_page.add_second_row() 
        assert exceptions_page.is_row2_isdisplayed(), "Row 2 should be displayed"
