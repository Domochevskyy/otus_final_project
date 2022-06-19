from selenium.webdriver.common.by import By


class AuthAdminPageLocators:
    username = (By.XPATH, '//input[@name="username"]')

    password = (By.XPATH, '//input[@name="password"]')

    login_button = (By.XPATH, '//button[@type="submit"]')


class AdminPageLocators:
    catalog_list = (By.XPATH, '//a[text()=" Catalog"]')

    products_link = (By.XPATH, '//ul[@id="collapse1"]//a[text()="Products"]')


class ProductsPageLocators:
    add_new = (By.XPATH, '//a[@data-original-title="Add New"]')

    product_name = (By.XPATH, '//input[@placeholder="Product Name"]')

    meta_tag_title = (By.XPATH, '//input[@placeholder="Meta Tag Title"]')

    data = (By.XPATH, '//a[text()="Data"]')

    model = (By.XPATH, '//input[@placeholder="Model"]')

    save = (By.XPATH, '//button[@type="submit"]')

    delete_product = (By.XPATH, '//button[@data-original-title="Delete"]')

    success_alert = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]/button')


class CustomersPageLocators:
    customers_parent = (By.XPATH, '//a[text()=" Customers"]')

    customers_link = (By.XPATH, '//ul[@id="collapse5"]//a[text()="Customers"]')

    delete_button = (By.XPATH, '//button[@data-original-title="Delete"]')

    success_alert = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]/button')
