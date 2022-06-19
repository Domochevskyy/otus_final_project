import abc
import logging

import allure
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        WebDriverException)
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(abc.ABC):
    element_load_timeout = 10
    small_timeout = 2
    host = None

    def __init__(self, driver: ChromeDriver | FirefoxDriver = None):
        self.driver = driver

    @allure.step('Find elements with locator {locator}')
    def find_elements(self, locator: tuple[By, str]) -> list[WebElement]:
        return WebDriverWait(self.driver, self.element_load_timeout).until(
            ec.presence_of_all_elements_located(locator),
            message=f'Can not find elements with locator {locator}')

    @allure.step('Find element with locator {locator}')
    def find_element(self, locator: tuple[By, str]) -> WebElement:
        return WebDriverWait(self.driver, self.element_load_timeout).until(
            ec.presence_of_element_located(locator),
            message=f'Can not find element with locator {locator}'
        )

    @allure.step('Click on element')
    def click(self, element: WebElement = None) -> None:
        WebDriverWait(self.driver, self.element_load_timeout).until(
            ec.element_to_be_clickable(element),
            message=f'Element {element.tag_name} is not clickable at the position {element.location}'
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            logging.info(f'{element.tag_name} is not clickable. Try an another one')

    @allure.step('Send {keys}')
    def send_keys(self, input_element: WebElement = None, keys: str | Keys = None) -> None:
        WebDriverWait(self.driver, self.element_load_timeout).until(
            ec.visibility_of(input_element),
            message=f'Element {input_element.tag_name} is not visible',
        )
        try:
            input_element.clear()
        except WebDriverException:
            logging.info(f'Can not clear {input_element.tag_name}')
        input_element.send_keys(keys)

    @allure.step('Open page with url {url}')
    def get(self, url: str):
        self.driver.get(url)
        logging.info(f'Redirect to {url}')
