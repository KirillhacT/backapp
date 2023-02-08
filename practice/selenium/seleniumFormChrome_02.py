from selenium import webdriver
from selenium.webdriver.common.by import By
from main_01 import path
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Biba")

# driver = webdriver.Chrome(executable_path=path, options=options)commit


with webdriver.Chrome(executable_path=path, options=options) as driver:
    driver.get("https://github.com/login")
    email_input = driver.find_element(By.ID, "login_field")
    email_input.clear()
    email_input.send_keys("GGWP")

    login_input = driver.find_element(By.ID, "password")
    login_input.clear()
    login_input.send_keys("12345")

    driver.find_element(By.NAME, "commit").click()

    example_element = driver.find_element(By.CLASS_NAME, "js-flash-alert")
    # print(example_element.text) #Текст
    # print(example_element.get_attribute("role")) #Берем атрибут из нашего элемента
    sleep(100)