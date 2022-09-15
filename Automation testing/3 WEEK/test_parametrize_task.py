import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX


def answer():
    return math.log(int(time.time()))


@pytest.mark.parametrize("page", ["236895", "236896",
                                  "236897", "236898",
                                  "236899", "236903",
                                  "236904", "236905"])
def test_ufo_comments(browser, page):
    url = f"https://stepik.org/lesson/{page}/step/1"
    result = answer()
    browser.get(url)
    page = browser.find_element(By.CLASS_NAME, "ember-text-area")
    page.send_keys(result)
    subbutton = WebDriverWait(browser, 10).until(EX.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    subbutton.click()
    res = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert res == "Correct!", f"{res}"



