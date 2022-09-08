from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os


def filepath():
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
    # print(file_path)
    return file_path

url = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    firstName = browser.find_element(By.NAME,"firstname")
    firstName.send_keys("Billy Joe")
    lastName = browser.find_element(By.NAME, "lastname")
    lastName.send_keys("Armstrong")
    emailAddress = browser.find_element(By.NAME, "email")
    emailAddress.send_keys("bja@greenday.com")
    with open('test.txt', 'w') as file:
        path = filepath()
    uploadFile = browser.find_element(By.CSS_SELECTOR,"[type=\"file\"]")
    uploadFile.send_keys(path)
    submitBtn = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    submitBtn.click()
finally:
    sleep(5)
    browser.quit()