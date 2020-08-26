import pytest
import time
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}" for num in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.add_to_cart_message_should_be_correct()
    page.cart_total_is_correct()

