import requests
from bs4 import BeautifulSoup
import json

def get_data(url):
    # req = requests.get(url)
    # with open("file1.html", "w", encoding="utf-8") as file:
    #         file.write(req.text)

    with open("file1.html", encoding="utf-8") as file:
        src = file.read()
            
    soup = BeautifulSoup(src, "lxml")
    list_names = soup.find(id="dle-content").find_all(class_="header-h1")
    project_urls = []
    for name in list_names:
        url = name.find("a").get("href")
        project_urls.append(url)
    # print(project_urls[3].split("/")[4][5:-5])


    for url in project_urls:
        req = requests.get(url)

        with open(f"data/{url.split('/')[4][5:-5]}.html", "w") as file:
            file.write(req.text)

        # with open(f"data/{url.split('/')[4][5:-5]}", "w") as file:
        #     file.wite(req.text)

        # soup2 = BeautifulSoup(src, "lxml")
        # options = soup2.find("div", class_="quote").find_all("p")
        # dict_names = {}
        # for opt in options:
        #     a = str(opt.text)
        #     mas = a.split(":")
        #     dict_names[mas[0]] = mas[1].strip()[:-1]
        # print(dict_names)

    #     with open("current.html", encoding="utf-8") as file:
    #         src = file.read()
    
        
get_data("https://freetp.org/")