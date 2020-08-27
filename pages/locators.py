from selenium.webdriver.common.by import By


class Urls:
    MAIN_PAGE = 'http://selenium1py.pythonanywhere.com/'


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span > a')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.basket-mini')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1)')


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//p[contains(text(), "basket is empty")]')
