import allure
import pytest

from opencart_lib.models import CurrencyChoice, CurrencyType


class TestMainPage:
    currency_displays = list(map(lambda currency: currency.value, CurrencyType))
    currency_choices = list(map(lambda currency: currency, CurrencyChoice))
    searched_product = 'imac'
    nav_bar_links = [
        'Desktops', 'Laptops & Notebooks',
        'Components', 'Tablets',
        'Software', 'Phones & PDAs',
        'Cameras', 'MP3 Players'
    ]

    @allure.title('Changing currency')
    @pytest.mark.parametrize(argnames='currency_type, currency_choice',
                             argvalues=zip(currency_displays, currency_choices))
    def test_currency(self, currency_type, currency_choice, main_page):
        """Test for changing currency on the main page."""
        with allure.step('Get main page'):
            main_page.get(main_page.url)
        main_page.currency = currency_choice
        assert main_page.currency == currency_type, 'Currency was not changed.'

    @allure.title('Main page title')
    def test_title(self, main_page):
        """Test for main page title."""
        assert main_page.title == main_page.driver.title, 'Main page title is invalid.'

    @allure.title('Searching product in maim page')
    def test_search(self, main_page, search_page):
        """Test for searching product in main page."""
        main_page.search_product(self.searched_product)
        products = search_page.find_results()
        assert len(products) == 1, f'{self.searched_product} is not found.'

    @allure.title('Navigation bar elements')
    def test_nav_bar(self, main_page):
        """Test for checking navigation bar elements."""
        with allure.step('Get main page'):
            main_page.get(main_page.url)
        elements = main_page.nav_bar
        assert main_page.text_from(elements), 'Nav bar elements are invalid.'

    @allure.title('Shopping cart')
    def test_empty_cart(self, main_page):
        """Checking shopping cart is empty by default."""
        result_msg = 'Your shopping cart is empty!'
        msg = main_page.get_shopping_cart_products()
        assert msg == result_msg, 'Shopping cart is not empty by default.'
