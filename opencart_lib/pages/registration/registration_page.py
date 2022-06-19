import logging

import allure
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver

from opencart_lib.models import User

from ..base.base_page import BasePage
from .registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def __init__(self, driver: ChromeDriver | FirefoxDriver = None):
        super().__init__(driver=driver)
        self.url = f'http://{self.host}/index.php?route=account/register'

    @allure.step('Register account {user}')
    def register_account(self, user: User):
        first_name = self.find_element(RegistrationPageLocators.first_name)
        self.send_keys(input_element=first_name, keys=user.first_name)
        last_name = self.find_element(RegistrationPageLocators.last_name)
        self.send_keys(input_element=last_name, keys=user.last_name)
        email = self.find_element(RegistrationPageLocators.email)
        self.send_keys(input_element=email, keys=user.email)
        phone = self.find_element(RegistrationPageLocators.telephone)
        self.send_keys(input_element=phone, keys=user.telephone)
        password = self.find_element(RegistrationPageLocators.password)
        self.send_keys(input_element=password, keys=user.password)
        confirm_password = self.find_element(RegistrationPageLocators.confirm_password)
        self.send_keys(input_element=confirm_password, keys=user.password)

        agree_input = self.find_element(RegistrationPageLocators.agree_policy)
        self.send_keys(input_element=agree_input, keys=Keys.SPACE)
        continue_button = self.find_element(RegistrationPageLocators.continue_button)
        self.click(element=continue_button)
        logging.info(f'Account {user} was successfully registered.')
