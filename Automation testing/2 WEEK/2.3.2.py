from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

url = 'http://suninjuly.github.io/alert_accept.html'


def formula(value):
    return math.log(abs(12 * math.sin(value)))


try:
    browser = webdriver.Chrome()
    browser.get(url)
    firstBtn = browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    sleep(1)
    firstBtn.click()
    alertWindow = browser.switch_to.alert
    sleep(1)
    alertWindow.accept()
    x = browser.find_element(By.ID, "input_value").text
    result = formula(int(x))
    answerField = browser.find_element(By.ID, "answer")
    answerField.send_keys(result)
    submitBtn = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    submitBtn.click()
finally:
    sleep(5)
    browser.quit()