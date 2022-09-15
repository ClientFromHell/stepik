import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('language', ['ru', 'en-gb'])
def test_site_lang(browser, language):
    url = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

