from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def should_be_message_about_empty_basket(self):
		expected_msg = BasketPageLocators.EMPTY_BASKET_MSG
		current_msg = self.browser.find_element(*BasketPageLocators.BASKET_CONTAIN).text
		assert expected_msg in current_msg, f"'{expected_msg}' is not contained in '{current_msg}'"

	def should_absent_items_by_now(self):
		assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BY_NOW), \
			"Message about items in basket is present, but it should not be"

