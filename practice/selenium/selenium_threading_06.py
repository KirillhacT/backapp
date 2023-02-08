from selenium import webdriver
from selenium.webdriver.common.by import By
from main_01 import path
from time import sleep
from multiprocessing import Pool

url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
options = webdriver.ChromeOptions()

options.add_argument("user-agent=None")
options.add_argument("--disable-blink-features=AutomationControlled")



# urls_list = ["https://stackoverflow.com", "https://github.com", "https://vk.com"]
# def get_data(url: str):
#     try:
#         driver = webdriver.Chrome(executable_path=path, options=options)
#         driver.get(url)
#         sleep(8)
#         driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
# if __name__ == '__main__':
#     p = Pool(processes=3)
#     p.map(get_data, urls_list)

