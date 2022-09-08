from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

url = "http://SunInJuly.github.io/execute_script.html"


def formula(value):
    return math.log(abs(12 * math.sin(value)))


try:
    browser = webdriver.Chrome()
    browser.get(url)
    x = browser.find_element(By.ID, "input_value").text
    # print(x)
    answerField = browser.find_element(By.ID, "answer")
    answerField.send_keys(formula(int(x)))
    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()
    submitBtn = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submitBtn)
    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()
    submitBtn.click()

finally:
    sleep(3)
    browser.quit()