from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# url = 'http://suninjuly.github.io/registration1.html'
url = 'http://suninjuly.github.io/registration2.html'
try:
    browser = webdriver.Chrome()
    browser.get(url)
    firstName = browser.find_element(By.CSS_SELECTOR, "[placeholder=\"Input your first name\"]")
    firstName.send_keys('Billy Joe')
    secondName = browser.find_element(By.CSS_SELECTOR, "[placeholder=\"Input your last name\"]")
    secondName.send_keys('Armstrong')
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder=\"Input your email\"]")
    email.send_keys('billy.joe@greenday.com')
    # phone = browser.find_element(By.CSS_SELECTOR, "[placeholder=\"Input your phone:\"]")
    # phone.send_keys('+18357-2330-3334')
    # address = browser.find_element(By.CSS_SELECTOR, "[placeholder=\"Input your address:\"]")
    # address.send_keys('LA, Flowers boulevard 4th')
    submitbtn = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    submitbtn.click()
    sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    sleep(3)
    browser.quit()
