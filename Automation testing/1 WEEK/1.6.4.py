from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    form_elements = browser.find_elements(By.CSS_SELECTOR, "[type=\"text\"]")
    for index, value in enumerate(form_elements):
        value.send_keys(f'{index} - Some data')
    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    button.click()
finally:
    sleep(10)
    browser.quit()

