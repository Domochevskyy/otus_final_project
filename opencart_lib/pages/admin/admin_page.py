import logging

import allure
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver

from opencart_lib.models import AuthData, User

from ..base.base_page import BasePage
from .admin_page_locators import (AdminPageLocators, AuthAdminPageLocators,
                                  CustomersPageLocators, ProductsPageLocators)


class AuthAdminPage(BasePage):
    title = 'Administration'

    def __init__(self, driver: ChromeDriver | FirefoxDriver = None):
        super().__init__(driver=driver)
        self.url = f'http://{self.host}/admin'

    @allure.step('Login as {login} with password {password}')
    def login(self, login: AuthData.LOGIN = None, password: AuthData.PASSWORD = None) -> None:
        username_field = self.find_element(AuthAdminPageLocators.username)
        self.send_keys(input_element=username_field, keys=login)
        password_field = self.find_element(AuthAdminPageLocators.password)
        self.send_keys(input_element=password_field, keys=password)
        login_button = self.find_element(AuthAdminPageLocators.login_button)
        self.click(element=login_button)
        logging.info(f'Login as {login}')


class ProductsPage(BasePage):
    def __init__(self, driver: ChromeDriver | FirefoxDriver = None):
        super().__init__(driver=driver)

    @allure.step('Add product with name {name}, tag {tag_title} and model {model}')
    def add_product(self, name: str = None, tag_title: str = None, model: str = None) -> None:
        self._prepare_page()
        add_product_button = self.find_element(ProductsPageLocators.add_new)
        self.click(add_product_button)
        product_name_input = self.find_element(ProductsPageLocators.product_name)
        self.send_keys(input_element=product_name_input, keys=name)
        meta_tag_title_input = self.find_element(ProductsPageLocators.meta_tag_title)
        self.send_keys(input_element=meta_tag_title_input, keys=tag_title)
        data_input = self.find_element(ProductsPageLocators.data)
        self.click(data_input)
        model_input = self.find_element(ProductsPageLocators.model)
        self.send_keys(input_element=model_input, keys=model)
        save_button = self.find_element(ProductsPageLocators.save)
        self.click(save_button)
        logging.info(f'Product {name} successfully added.')

    @allure.step('Delete product with name {product_name}')
    def delete_product(self, product_name: str = None) -> None:
        self._prepare_page()
        element_checkbox_locator = f'//tr[td[text()="{product_name}"]]/td/input'
        product = self.find_element((By.XPATH, element_checkbox_locator))
        self.send_keys(input_element=product, keys=Keys.SPACE)
        delete_button = self.find_element(ProductsPageLocators.delete_product)
        self.click(delete_button)
        a = Alert(self.driver)
        a.accept()
        logging.info(f'Product {product_name} successfully deleted.')

    @allure.step('Prepare products page')
    def _prepare_page(self) -> None:
        catalog = self.find_element(AdminPageLocators.catalog_list)
        self.click(catalog)
        products = self.find_element(AdminPageLocators.products_link)
        self.click(products)
        logging.info('Open products page.')

    @allure.step('Trying to find product with name {name}')
    def is_product_found(self, name: str = None) -> bool:
        logging.info(f'Trying to find product with name {name}')
        product_locator = f'//td[3][text()="{name}"]'
        try:
            self.driver.find_element(By.XPATH, product_locator)
            return True
        except WebDriverException:
            return False


class CustomersPage(BasePage):
    def __init__(self, driver: ChromeDriver | FirefoxDriver = None):
        super().__init__(driver=driver)

    @allure.step('Delete customer with name {first_name} {last_name}')
    def delete(self, first_name: User.first_name, last_name: User.last_name) -> None:
        self._prepare_page()
        customer_locator = f'//tr[td[2][text()="{first_name} {last_name}"]]/td[1]'
        try:
            customer_input = self.driver.find_element(By.XPATH, customer_locator)
            self.click(element=customer_input)
        except WebDriverException:
            raise WebDriverException(f'Can not find user: {first_name} {last_name}')
        delete_button = self.find_element(CustomersPageLocators.delete_button)
        self.click(element=delete_button)
        Alert(self.driver).accept()
        logging.info(f'Customer {first_name} {last_name} successfully deleted.')

    @allure.step('Prepare customers page')
    def _prepare_page(self) -> None:
        customers_parent = self.find_element(CustomersPageLocators.customers_parent)
        self.click(element=customers_parent)
        customers = self.find_element(CustomersPageLocators.customers_link)
        self.click(element=customers)
        logging.info('Open castomers page')

    @allure.step('Trying to find customer with name {first_name} {last_name}')
    def is_customer_found(self, first_name: User.first_name, last_name: User.last_name) -> bool:
        self._prepare_page()
        logging.info(f'Trying to find customer with name {first_name} {last_name}')
        customer_locator = f'//tr[td[2][text()="{first_name} {last_name}"]]/td[1]'
        try:
            self.driver.find_element(By.XPATH, customer_locator)
            return True
        except WebDriverException:
            return False


class AdminPage(BasePage):

    def __init__(self, driver: ChromeDriver | FirefoxDriver = None):
        super().__init__(driver=driver)
        self.auth_admin_page = AuthAdminPage(driver)
        self.product_page = ProductsPage(driver)
        self.customers_page = CustomersPage(driver)
