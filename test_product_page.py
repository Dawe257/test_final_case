import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import LoginPageLocators, ProductPageLocators


@pytest.mark.need_review
@pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}" for num in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.add_to_cart_message_should_be_correct()
    page.cart_total_is_correct()


def test_success_message_is_not_presented(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappeared()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_empty()
    page.should_be_message_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LoginPageLocators.LOGIN_URL
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + "@mail.ru", '65a4dfga56gasd')
        page.should_be_success_register_message()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_URL
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_URL
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        # page.solve_quiz_and_get_code()
        page.add_to_cart_message_should_be_correct()
        page.cart_total_is_correct()
