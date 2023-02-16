import asyncio
import aiohttp
import time

start_time = time.time()

all_data = [] #Создаем массив данных
async def get_page_data(session, category: str, page_id: int) -> str:
    if page_id:
        url = f"https://www.ozon.ru/brand/{category}/?page={page_id}"
    else:
        url = f"https://www.ozon.ru/brand/{category}/"
    async with session.get(url) as responce: #Берем асинхронный ответ от сервера
        # assert responce.status == 200
        print(f"get url {url}")
        responce_text = await responce.text() #Ожидаем от него text
        all_data.append(responce_text) #Добавляем в массив данных
        return responce_text

async def load_site_data():
    categories_list = ['playstation-79966341', 'adidas-144082850', 'bosch-7577796', 'lego-19159896']
    async with aiohttp.ClientSession() as session: # Создает сессию (обращается к серверу асинхронно)
        tasks = [] #Создаем список задач
        for category in categories_list:
            for page_id in range(100):
                task = asyncio.create_task(get_page_data(session, category, page_id))
                tasks.append(task) #Добавляем задачу в список задач
        await asyncio.gather(*tasks) #Собираем полученные задачи


# load_site_data()
asyncio.run(load_site_data())
end_time = time.time() - start_time
print(end_time)