from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

url = 'http://suninjuly.github.io/wait2.html'

browser = webdriver.Chrome()
browser.get(url)
verifyBtn = WebDriverWait(browser,3).until(es.element_to_be_clickable((By.ID, "verify")))
verifyBtn.click()

