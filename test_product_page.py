from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.locators import LoginPageLocators
import pytest
import time


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)

    def setup(self, browser):

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        self.link = link
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + '@fakeMail.org', LoginPageLocators.TEST_PASSWORD)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):

        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):

        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_cart_page()
        page.should_the_same_titles_in_cart_and_added_product()
        page.should_the_same_prices_in_cart_and_added_product()


@pytest.mark.need_review
@pytest.mark.parametrize('num', [1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, num):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(num)}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page.should_the_same_titles_in_cart_and_added_product()
    page.should_the_same_prices_in_cart_and_added_product()


@pytest.mark.parametrize('link', [pytest.param(
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",	marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):

    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):

    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [pytest.param(
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):

    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_message_about_empty_basket()
    page.should_absent_items_by_now()
