from .pages.product_page import ProductPage
import pytest
import time

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param(
#	                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#	                                  marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#def test_guest_can_add_product_to_basket(browser, link):
#	page = ProductPage(browser, link)
#	page.open()
#	page.go_to_cart_page()
#	page.should_the_same_titles_in_cart_and_added_product()
#	page.should_the_same_prices_in_cart_and_added_product()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
	# Открываем страницу товара
	# Добавляем товар в корзину
	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page = ProductPage(browser, link)
	page.open()
	page.go_to_cart_page()
	page.should_not_be_success_message()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):
	# Открываем страницу товара
	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
	# Открываем страницу товара
	# Добавляем товар в корзину
	# Проверяем, что нет сообщения об успехе с помощью is_disappeared
	page = ProductPage(browser, link)
	page.open()
	page.go_to_cart_page()
	page.should_dissapear_of_success_message()
