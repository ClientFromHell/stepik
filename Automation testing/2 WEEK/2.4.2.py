from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://suninjuly.github.io/cats.html'

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url)
    element = driver.find_element(By.ID, "button")
finally:
    driver.quit()