#Fast Api - веб фреймворк для пайтона
#Uvicorn - сервер, для нашего фреймворка

#Для подписи
import hmac
import hashlib
import base64

from fastapi import FastAPI, Form, Cookie
from fastapi.responses import Response
from typing import Optional

app = FastAPI()
bd_from_users = {
    "alexey@user.com": {
        "name": "Алексей", 
        "password": 'ac24b40dbe9b6a6a5418a6a1fcbdc2e9f1a33d6f05ba27f0079d0a6f9e508a5b', #12345
        "balance": "100",
    },
    "petr@user.com": {
        "name": "Петр", 
        "password": "87d509a6788236e30c27aee656918ee52c43a252c694f9fba6b66996e32ee1a3", #Diablo_535
        "balance": "999999",
    }
}
MEDIA = "text/html"
SECRET_KEY = "e45f5d3d08a28de68d3c142d2207438e11cf603d195ce1cb91d8640b0aaf296c5e9a17ce2ed7b00cacd9c6c39ef2dfe40e3f7410aa0b946450b66d64aca9457d637ab"
PASSWORD_SALT = "af4e61dac3e037a684eedb5d9000f9cd3df89d911cc8e2354f73d3f6552b0357"

def verify_password(username: str, password: str) -> bool:
    password_hash = hashlib.sha256((password + PASSWORD_SALT).encode()).hexdigest().lower()
    stored_password_hash = bd_from_users[username]["password"].lower()
    return password_hash == stored_password_hash


def sign_data(data: str) -> str:
    """Функция, возвращающая хеш"""
    return hmac.new(
        SECRET_KEY.encode(),
        msg=data.encode(),
        digestmod=hashlib.sha256
    ).hexdigest().upper()

def get_user_name_from_sigh_string(username_sigh: str) -> Optional[str]:
    """Если хеш юзера и хеш куки совпадают, то возращаем нашего юзера
    иначе None"""
    username_base64, sign = username_sigh.split(".")
    username = base64.b64decode(username_base64.encode()).decode()
    valid_sigh = sign_data(username)
    if hmac.compare_digest(valid_sigh, sign):
        return username

def responce_data(login_page, username):
    """
    1. Если куков нет, возвращаем страницу с авторизацией
    2. Проверяем юзернейм специальной функцией, и если он не валидный, удаляем куку и возвращаем страницу с авторизацией
    3. В противном случае пытаемся вытащить юзера из базы и возвращем страницу из куков
    4. Если произошла ошибка, кука удаляется и мы возвращаемся на исходную страницу
    """
    root = Response(login_page, media_type=MEDIA)
    try:
        if not username:
            return root
        valid_username = get_user_name_from_sigh_string(username)

        if not valid_username:
            responce = root
            responce.delete_cookie(key="username")
            return responce

        trying_username = bd_from_users[valid_username]
        return Response(f"Привет {trying_username['name']}!", media_type="text/html")
    except Exception as ex:  # Если пользователя нет, кука удалится
        responce = root
        responce.delete_cookie(key="username")
        return responce



@app.get("/")
def index_page(username: Optional[str] = Cookie(default=None)):
    with open("templates/index.html", "r", encoding="utf-8") as file:
        login_page = file.read()
    responce = responce_data(login_page, username)
    return responce

    

@app.post("/login")
def process_login_page(username : str = Form(...), password: str = Form(...)):
    # if users[username]["password"] == password: - так не нада
    user = bd_from_users.get(username) #Если ключа нема
    # if not user or user["password"] != password:
    if not user or not verify_password(username, password):
        return Response("Ты хто такой, С*ка?", media_type=MEDIA)
    name_user = user["name"]
    balance = user["balance"]
    responce = Response(f"Привет {name_user}!<br/> balance: {balance}", media_type=MEDIA)
    #Задаем cookie

    username_sigh = base64.b64encode(username.encode()).decode() + "." + \
        sign_data(username)
    responce.set_cookie(key='username', value=username_sigh)
    return responce