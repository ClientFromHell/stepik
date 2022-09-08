from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep

url = 'http://suninjuly.github.io/redirect_accept.html'


def formula(value):
    return math.log(abs(12 * math.sin(value)))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    flyBtn = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    flyBtn.click()
    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])
    x = browser.find_element(By.ID, "input_value").text
    result = formula(int(x))
    ansfield = browser.find_element(By.ID, "answer")
    ansfield.send_keys(result)
    subBtn = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    subBtn.click()
finally:
    sleep(5)
    browser.quit()