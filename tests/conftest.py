import logging

import allure
import pytest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Remote
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver

from opencart_lib.models import User
from opencart_lib.pages import (AdminPage, BasePage, MainPage,
                                RegistrationPage, SearchPage)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    try:
        if rep.when == 'call' and rep.failed:
            if 'browser' in item.fixturenames:
                web_browser = item.funcargs['browser']
                allure.attach(
                    web_browser.get_screenshot_as_png(),
                    name='screenshot',
                    attachment_type=allure.attachment_type.PNG
                )
            else:
                logging.info('Failed to get screenshot')

    except Exception as exception:
        logging.info(f'Failed to take screenshot: {exception}')


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Web browser', required=True)
    parser.addoption('--host', default='192.168.1.5:8081', help='Base opencart address: HOSTNAME:PORT.', required=True)
    parser.addoption('--driver_path')
    parser.addoption("--executor", action="store", default="selenoid")
    parser.addoption("--videos", default=False)
    parser.addoption("--vnc", default=True)
    parser.addoption("--logs", default=True)


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    BasePage.host = config.getoption('--host')


@pytest.fixture(scope='session')
def browser(request) -> ChromeDriver | FirefoxDriver:
    _browser = request.config.getoption('--browser').lower()
    driver_path = request.config.getoption('--driver_path')
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    if executor != 'local':
        executor_url = f"http://{executor}:4444/wd/hub"
        caps = {
            "browserName": _browser,
            "name": "Nikolay",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            }
        }
        _browser = Remote(command_executor=executor_url, desired_capabilities=caps)
    else:
        match _browser:
            case 'chrome':
                chrome_service = ChromeService(driver_path)
                _browser = ChromeDriver(service=chrome_service)
            case 'firefox':
                firefox_service = FirefoxService(driver_path)
                _browser = FirefoxDriver(service=firefox_service)
            case _:
                raise WebDriverException(msg='Invalid browser name.\nMake sure that name is chrome or firefox.')
        _browser.maximize_window()
    yield _browser
    _browser.close()
    _browser.quit()


@pytest.fixture()
def main_page(browser):
    return MainPage(browser)


@pytest.fixture()
def search_page(browser):
    return SearchPage(browser)


@pytest.fixture()
def admin_page(browser):
    return AdminPage(browser)


@pytest.fixture()
def registration_page(browser):
    return RegistrationPage(browser)


@pytest.fixture()
def delete_user(admin_page):
    yield
    admin_page.driver.refresh()
    admin_page.customers_page.delete(User.first_name, User.last_name)
