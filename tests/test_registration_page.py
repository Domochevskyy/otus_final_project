import allure

from opencart_lib.models import AuthData, User


class TestRegistrationPage:

    @allure.title('User registration')
    def test_registration(self, registration_page, admin_page, delete_user):
        """Checking user registration in Open Cart."""
        with allure.step('Get registration page'):
            registration_page.get(registration_page.url)
        registration_page.register_account(user=User)
        with allure.step('Get login page'):
            registration_page.driver.get(admin_page.auth_admin_page.url)
        admin_page.auth_admin_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        assert admin_page.customers_page.is_customer_found(User.first_name, User.last_name), 'Registration failed.'
