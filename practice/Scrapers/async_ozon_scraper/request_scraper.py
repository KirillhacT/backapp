import requests
import time

def get_page_data(category: str, page_id: int) -> str:
    if page_id:
        url = f"https://www.ozon.ru/brand/{category}/?page={page_id}"
    else:
        url = f"https://www.ozon.ru/brand/{category}/"
    print(f"get url {url}")
    responce = requests.get(url)
    return responce.text

def load_site_data():
    categories_list = ['playstation-79966341', 'adidas-144082850', 'bosch-7577796', 'lego-19159896']
    for category in categories_list:
        for page in range(2):
            text = get_page_data(category, page)
            with open(f"data/{category}-{page}.html", "w", encoding='utf-8') as file:
                file.write(text)

if __name__ == '__main__':
    load_site_data()
