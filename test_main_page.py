from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators


def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
	page = MainPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
	page = MainPage(browser, link)
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

