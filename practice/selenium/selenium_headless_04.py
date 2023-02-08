from selenium import webdriver
from selenium.webdriver.common.by import By
from main_01 import path
from time import sleep
from data import LOGIN, PASSWORD

options = webdriver.ChromeOptions()

options.add_argument("user-agent=None")
options.add_argument("--disable-blink-features=AutomationControlled")

#Загрузка браузера в фоновом режиме
options.add_argument("--headless")

url = "https://github.com/login"
with webdriver.Chrome(executable_path=path, options=options) as driver:
    driver.get(url)
    email_input = driver.find_element(By.ID, "login_field")
    email_input.clear()
    email_input.send_keys(LOGIN)
    sleep(1)

    login_input = driver.find_element(By.ID, "password")
    login_input.clear()
    login_input.send_keys(PASSWORD)
    sleep(1)
    print("Auth")

    driver.find_element(By.NAME, "commit").click()

    sleep(3)
    Class = "markdown-title"
    driver.find_element(By.CLASS_NAME, Class).click()
    print("Click")
    sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/div/a").click()

    sleep(100)