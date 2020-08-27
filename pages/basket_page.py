from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, 'This is not basket page'

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), 'Basket not empty, but should be'

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Empty basket message is not present'
