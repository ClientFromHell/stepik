from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


url = 'http://suninjuly.github.io/get_attribute.html'


def func(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get(url)
    treasure = browser.find_element(By.ID, "treasure")
    valuex = treasure.get_attribute("valuex")
    # print(valuex)
    result = func(int(valuex))
    answerField = browser.find_element(By.ID, "answer")
    answerField.send_keys(result)
    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()
    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()
    submitButton = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    submitButton.click()

finally:
    sleep(5)
    browser.quit()