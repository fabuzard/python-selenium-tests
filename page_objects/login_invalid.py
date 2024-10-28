from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class LoginInvalid(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID,"student")
    __password_field = (By.ID,"password")
    __submit_button = (By.XPATH,"//button[@class='btn']")

    def __init__(self,driver: WebDriver):
        super().__init__(driver)

    def execute_invalid_login(self, username: str, password: str):
        super()._type(self.__username_field,username)
        super()._type(self.__password_field,password)
        super()._click(self.__submit_button)
        