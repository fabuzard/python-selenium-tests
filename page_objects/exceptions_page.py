from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class ExceptionsPage(BasePage):

    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row_1_input_element = (By.XPATH, "//div[@id='row1']/input")
    __row_2_input_element = (By.XPATH, "//div[@id='row2']/input")
    __row_1_save_button = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row_2_save_button = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __confirmation_element = (By.ID, "confirmation")
    __edit_button = (By.ID, "edit_btn")
    __instruction_text = (By.XPATH, "//p[@id='instructions']")
    def __init__(self,driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row_2_input_element)

    def is_row2_isdisplayed(self)->bool:
        return super()._is_displayed(self.__row_2_input_element)
    
    def row2_input_element(self,food:str):
        super()._type(self.__row_2_input_element,food)
        super()._click(self.__row_2_save_button)
        super()._wait_until_element_is_visible(self.__confirmation_element)

    def get_confirmation_message(self)->str:
        return super()._get_text(self.__confirmation_element)
    
    def modify_row1_input(self,food:str):
        super()._click(self.__edit_button)
        super()._wait_until_element_is_clickable(self.__row_1_input_element)
        super()._clear(self.__row_1_input_element)
        super()._type(self.__row_1_input_element,food)
        super()._click(self.__row_1_save_button)
        super()._wait_until_element_is_visible(self.__confirmation_element)

    def are_instruction_displayed(self)->bool:
        return super()._is_displayed(self.__instruction_text)