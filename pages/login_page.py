from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, f'"login" is absent in "{self.browser.current_url}"'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login = self.is_element_present(*LoginPageLocators.CURRENT_EMAIL_ADDRESS)
        password = self.is_element_present(*LoginPageLocators.CURRENT_PASSWORD)
        btn = self.is_element_present(*LoginPageLocators.ENTER_BUTTON)
        assert login and password and btn, 'Problem with login form, check e-mail, password, enter-button fields'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        new_login = self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_ADDRESS)
        password_1 = self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        password_2 = self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        btn = self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON)
        assert new_login and password_1 and password_2 and btn, 'Problem with registration form, check: ' \
                                                                'new_login, password_1, password_2, ' \
                                                                'registration-button fields'