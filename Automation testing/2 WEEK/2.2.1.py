from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from time import sleep

url = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    # select = browser.find_element(By.ID, "dropdown")
    # select.click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f"{int(num1) + int(num2)}")

    # valueinselect = browser.find_element(By.XPATH, f"//option[text()=\"{int(num1) + int(num2)}\"]")
    # valueinselect.click()
    submitbtn = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    submitbtn.click()
finally:
    sleep(5)
    browser.quit()