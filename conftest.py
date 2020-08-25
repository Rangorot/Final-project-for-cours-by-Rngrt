import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language for browser")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options,
                               executable_path='D:\pythonP\тестирование\drivers\chrome\chromedriver.exe')
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()