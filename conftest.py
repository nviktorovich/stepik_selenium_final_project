import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
	parser.addoption('--language', action='store', default=en-gb, help="Choose test language: ru, es, en-gb, ...")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if language != None and language != '':
        browser = webdriver.Chrome(options=options)
        print("\nopen browser..")
    else:
        raise pytest.UsageError('example of correct command:>>pytest -s -v --language=[select_language] test_items.py')
    yield browser
    print("\nquit browser..")
    browser.quit()
