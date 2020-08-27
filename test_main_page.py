import pytest
from .pages.locators import Urls
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_can_do_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()


@pytest.mark.smoke
def test_guest_can_see_product_in_basket_opened_from_main_page(browser):
    link = Urls.MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_empty()
    page.should_be_message_empty_basket()
