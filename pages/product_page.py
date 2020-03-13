from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

	def go_to_cart_page(self):
		add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
		add_to_cart_button.click()
		self.solve_quiz_and_get_code()

	def should_the_same_titles_in_cart_and_added_product(self):
		added_product = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TITLE).text
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
		assert added_product == product_name, f'different between product:"{product_name}" and "{added_product}"'

	def should_the_same_prices_in_cart_and_added_product(self):
		total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		assert total_price == product_price, f'different between prices "{total_price} and {product_price}"'

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
			"Success message is presented, but should not be"

	def should_dissapear_of_success_message(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
		    "Success message is not disappeared"