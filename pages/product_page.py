from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

	def go_to_cart_page(self):
		add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
		add_to_cart_button.click()
		self.solve_quiz_and_get_code()

		added_product = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TITLE).text
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
		total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

		assert added_product == product_name, f'different between product:"{product_name}" and "{added_product}"'
		assert total_price == product_price, f'different between prices "{total_price} and {product_price}"'
		#time.sleep(2)