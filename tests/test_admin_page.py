import allure

from opencart_lib.models import AuthData


class TestAdminPage:

    @allure.title('Add product')
    def test_add_product(self, admin_page):
        """Test for adding a product in the catalog list."""
        with allure.step('Get login page'):
            admin_page.get(admin_page.auth_admin_page.url)
        admin_page.auth_admin_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        admin_page.product_page.add_product(name='a', tag_title='a', model='a')
        assert admin_page.product_page.is_product_found('a'), 'Product "a" was not added.'

    @allure.title('Delete product')
    def test_delete_product(self, admin_page):
        """Test for deleting a product in the catalog list."""
        admin_page.product_page.delete_product('a')
        assert not admin_page.product_page.is_product_found('a'), 'Product "a" was not deleted.'
