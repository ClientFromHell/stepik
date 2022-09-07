from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

url = 'https://suninjuly.github.io/math.html'


def x_resulter(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get(url)
    x = browser.find_element(By.ID, "input_value").text
    formula = browser.find_element(By.XPATH, "//div[1]/label/span[1]").text
    result = x_resulter(int(x))
    inputField = browser.find_element(By.ID, "answer")
    inputField.send_keys(result)
    checkBox = browser.find_element(By.ID, "robotCheckbox")
    checkBox.click()
    radioBox = browser.find_element(By.ID, "robotsRule")
    radioBox.click()
    submitBtn = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    submitBtn.click()


finally:
    sleep(5)
    browser.quit()


