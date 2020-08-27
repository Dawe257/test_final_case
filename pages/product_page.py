from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def add_to_cart_message_should_be_correct(self):
        add_to_cart_message = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert add_to_cart_message == item_name, 'Message is not correct'

    def cart_total_is_correct(self):
        cart_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert item_price in cart_total, 'Cart total amount is not correct'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            'Success message is presented, but should not be'

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            'Success message is presented, but should disappeared'
