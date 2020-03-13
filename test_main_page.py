from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():

	def test_guest_can_go_to_login_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"
		page = BasePage(browser, link)
		page.open()
		page.go_to_login_page()
		login_page = LoginPage(browser, browser.current_url)
		login_page.should_be_login_page()

	def test_guest_should_see_login_link(self,browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"
		page = BasePage(browser, link)
		page.open()
		page.should_be_login_link()





def test_guest_should_see_correct_login_url(browser):
	page = LoginPage(browser, LoginPageLocators.LOGIN_AND_REGISTRATION_FORM_URL)
	page.open()
	page.should_be_login_url()


def test_guest_can_fill_the_login_form(browser):
	page = LoginPage(browser, LoginPageLocators.LOGIN_AND_REGISTRATION_FORM_URL)
	page.open()
	page.should_be_login_form()


def test_guest_can_registred_new_user(browser):
	page = LoginPage(browser, LoginPageLocators.LOGIN_AND_REGISTRATION_FORM_URL)
	page.open()
	page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = BasketPage(browser, link)
	page.open()
	page.go_to_basket_page()
	page.should_be_message_about_empty_basket()
	page.should_absent_items_by_now()