import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', help="Choose language")

    
@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    # options.add_argument('--headless')
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print('\nStart browser for test...')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print('\nClose browser...')
    browser.quit()
