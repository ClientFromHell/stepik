from selenium import webdriver
from selenium.webdriver.common.by import By as by
import time
import math


def typeforms():
    input_fn = browser.find_element(by.NAME, "first_name")
    input_fn.send_keys('Sergey')
    input_ln = browser.find_element(by.NAME, "last_name")
    input_ln.send_keys('Zheludev')
    input_city = browser.find_element(by.CLASS_NAME, "city")
    input_city.send_keys('Minsk')
    input_country = browser.find_element(by.ID, "country")
    input_country.send_keys('Belarus')
    submit_btn = browser.find_element(by.CSS_SELECTOR, "button.btn")
    submit_btn.click()


url = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    search_url = browser.find_element(by.LINK_TEXT,str(math.ceil(math.pow(math.pi, math.e)*10000)))
    search_url.click()
    typeforms()
finally:
    time.sleep(5)
    browser.quit()