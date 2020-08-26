from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_do_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    # page = MainPage(browser, link)
    # page.open()
    # page.should_be_login_link()
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()
