# CHAPTER 1
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
#
# @pytest.fixture(scope="function")
# def browser():
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(10)
#     yield browser
#     # sleep(10)
#     browser.quit()

# CHAPTER 2
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = Options()
        options.add_argument("--width=800")
        options.add_argument("--height=500")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    sleep(3)
    browser.quit()