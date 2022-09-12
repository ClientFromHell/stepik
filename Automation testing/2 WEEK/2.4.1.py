from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://suninjuly.github.io/wait1.html'

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)

verifyBtn = driver.find_element(By.ID, "verify")
verifyBtn.click()
verifymessaege = driver.find_element(By.ID, "verify_message").text

assert verifymessaege == "Verification was successful!"

sleep(5)
driver.quit()