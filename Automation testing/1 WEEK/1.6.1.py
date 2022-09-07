from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/simple_form_find_task.html"

def typeform():
    input_fn = browser.find_element(By.NAME, "first_name")
    input_fn.send_keys('Sergey')
    input_ln = browser.find_element(By.NAME, "last_name")
    input_ln.send_keys('Zheludev')
    input_city = browser.find_element(By.CLASS_NAME, "city")
    input_city.send_keys('Minsk')
    input_country = browser.find_element(By.ID, "country")
    input_country.send_keys('Belarus')
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()


try:
    browser = webdriver.Chrome()
    browser.get(url)
    input_fn = browser.find_element(By.NAME, "first_name")
    input_fn.send_keys('Sergey')
    input_ln = browser.find_element(By.NAME, "last_name")
    input_ln.send_keys('Zheludev')
    input_city = browser.find_element(By.CLASS_NAME, "city")
    input_city.send_keys('Minsk')
    input_country = browser.find_element(By.ID, "country")
    input_country.send_keys('Belarus')
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()
    time.sleep(5)
finally:
    browser.quit()
