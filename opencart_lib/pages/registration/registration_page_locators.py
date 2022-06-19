from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    first_name = (By.XPATH, '//input[@name="firstname"]')

    last_name = (By.XPATH, '//input[@name="lastname"]')

    email = (By.XPATH, '//input[@name="email"]')

    telephone = (By.XPATH, '//input[@name="telephone"]')

    password = (By.XPATH, '//input[@name="password"]')

    confirm_password = (By.XPATH, '//input[@name="confirm"]')

    agree_policy = (By.XPATH, '//input[@type="checkbox"]')

    continue_button = (By.XPATH, '//input[@type="submit"]')

    success_message = (By.XPATH, '//h1[text()="Your Account Has Been Created!"]')
