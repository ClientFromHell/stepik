from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://suninjuly.github.io/huge_form.html'


try:
    browser = webdriver.Chrome()
    browser.get(url)
    form_elements = browser.find_elements(By.TAG_NAME, "input")
    for element in form_elements:
        element.send_keys('SOME_Information')
    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    button.click()
finally:
    sleep(3)
    browser.quit()
