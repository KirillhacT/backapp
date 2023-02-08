from selenium import webdriver
from selenium.webdriver.common.by import By

path = r"/backapp/BIG_PRACTICE/selenium/сhromedriver/chromedriver.exe"

url = "https://parsinger.ru/selenium/7/7.html"
with webdriver.Chrome(executable_path=path) as browser:
    browser.get(url=url)
    sum = 0
    block = browser.find_elements(By.TAG_NAME, "option")
    for i in block:
        sum += int(i.text)

    input_res = browser.find_element(By.ID, "input_result")
    input_res.send_keys(str(sum))

    browser.find_element(By.ID, "sendbutton").click()

