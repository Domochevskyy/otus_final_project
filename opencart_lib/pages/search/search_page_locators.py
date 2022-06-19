from selenium.webdriver.common.by import By


class SearchPageLocators:
    searched_items_links = (By.XPATH, '//div/div[@class="product-thumb"]/div[2]/div/h4/a')

    non_result_message = (By.XPATH, '//p[text()="There is no product that matches the search criteria."]')
