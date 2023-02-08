from selenium import webdriver
from selenium.webdriver.common.by import By
from main_01 import path
from time import sleep

url = "https://www.avito.ru/borovichi?q=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B8"
options = webdriver.ChromeOptions()

options.add_argument("user-agent=None")
options.add_argument("--disable-blink-features=AutomationControlled")

with webdriver.Chrome(executable_path=path, options=options) as driver:
    driver.get(url=url)
    print(f"Currectly url: {driver.current_url}")
    #Доступ к вкладкам
    # print(driver.window_handles)

    #Умное ожидание, заканчивается, если элемент загрузился
    driver.implicitly_wait(5)
    # sleep(5)
    items = driver.find_elements(By.XPATH, '//div[@data-marker="item-photo"]')
    #Показывает список вкладок
    # print(driver.window_handles)

    # Example
    # print(f"Currectly url: {driver.current_url}")
    # driver.switch_to.window(driver.window_handles[1])

    items[0].click()
    sleep(5)
    # username = driver.find_element(By.XPATH, '//div[@data-marker="seller-info/label"]')
    # print(username.text)
    # Закрываем текущую вкладку
    driver.switch_to.window(driver.window_handles[0])
    sleep(5)
    items[1].click()
    sleep(5)
    # username = driver.find_element(By.XPATH, '//div[@data-marker="seller-info/label"]')
    # print(username.text)


    sleep(100)
