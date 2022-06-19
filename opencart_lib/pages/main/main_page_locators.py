from selenium.webdriver.common.by import By


class MainPageLocators:
    currency_type = (By.XPATH, '//form[@id="form-currency"]/div/button/strong')

    currency_button = (By.XPATH, '//button[@class="btn btn-link dropdown-toggle"]')

    euro = (By.XPATH, '//button[@name="EUR"]')

    pound = (By.XPATH, '//button[@name="GBP"]')

    dollar = (By.XPATH, '//button[@name="USD"]')

    search_input = (By.XPATH, '//input[@name="search"]')

    search_button = (By.XPATH, '//button[@class="btn btn-default btn-lg"]')

    nav_bar = (By.XPATH, '//div[@class="collapse navbar-collapse navbar-ex1-collapse"]/ul/li')

    shopping_cart = (By.XPATH, '//*[@id="cart"]/button')

    empty_shopping_cart_msg = (By.XPATH, '//*[@id="cart"]/ul/li/p')
