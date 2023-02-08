from selenium import webdriver
from selenium.webdriver.common.by import By
from main_01 import path
from time import sleep

url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
options = webdriver.ChromeOptions()

options.add_argument("user-agent=None")

#Для старых браузеров
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

options.add_argument("--disable-blink-features=AutomationControlled")

with webdriver.Chrome(executable_path=path, options=options) as driver:
    driver.get(url=url)
    sleep(10)