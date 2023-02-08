from selenium import webdriver
import time

url = "https://www.youtube.com/"
url2 = "https://whatmyuseragent.com/"
path = r"/backapp/BIG_PRACTICE/selenium/сhromedriver/chromedriver.exe"

def main():
    # Создаем объект опций и добавляем аргумент user-agent
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=HelloWorld")
    # Добавляем прокси
    # options.add_argument(f"--proxy-server={ip}") #Сюда прописываем ip

    # Самая важная строка, прописываем веб драйвер
    browser = webdriver.Chrome(
        executable_path=path,
        options=options,
    )

    try:
        # browser.get(url=url)
        # browser.get(url=url2)
        browser.get(url="https://2ip.ru/")
        time.sleep(5)
        # browser.refresh() #Обновляет страничку браузера

        #Скриншот в браузере
        # browser.get_screenshot_as_file(1.png)
        # browser.save_screenshot('2.png')
    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()
if __name__ == "__main__":
    main()

