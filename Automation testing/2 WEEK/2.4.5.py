import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from math import sin, log
from time import sleep

url = 'http://suninjuly.github.io/explicit_wait2.html'


def formula(value):
    return log(abs(12 * sin(value)))


try:
    browser = webdriver.Chrome()
    browser.get(url)
    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 12).until(
        es.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    x = int(browser.find_element(By.ID, "input_value").text)
    result = formula(x)
    ansField = browser.find_element(By.ID, "answer")
    ansField.send_keys(result)
    submitBtn = browser.find_element(By.ID, "solve")
    submitBtn.click()
finally:
    sleep(5)
    browser.quit()


