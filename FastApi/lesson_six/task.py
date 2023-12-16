"""Ваша задача - создать приложение FastAPI, которое реализует аутентификацию на основе файлов cookie. Выполните следующие действия:

1. Создайте простой маршрут входа в систему по адресу "/login", который принимает имя пользователя и пароль в качестве данных формы. 
Если учетные данные действительны, установите безопасный файл cookie только для HTTP с именем "session_token" с уникальным значением.

2. Реализуйте защищенный маршрут в "/user", который требует аутентификации с использованием файла cookie "session_token". 
Если файл cookie действителен и содержит правильные данные аутентификации, верните ответ в формате JSON с информацией профиля пользователя.

3. Если файл cookie "session_token" отсутствует или недействителен, 
маршрут "/user" должен возвращать ответ об ошибке с кодом состояния 401 (неавторизован) или сообщение {"message": "Unauthorized"}.

Пример:

POST-запрос в `/login` с данными формы:

{
  "username": "user123"
  "password": "password123"
} 
Ответ должен содержать файл cookie "session_token".

GET-запрос к `/user` с помощью файла cookie "session_token":

session_token: "abc123xyz456"
Ответ должен возвращать информацию профиля пользователя.

GET-запрос к `/user` без файла cookie "session_token" или с недопустимым файлом cookie, например:

session_token: "invalid_token_value"
Ответ должен возвращать сообщение об ошибке с кодом состояния 401 или сообщение {"message": "Unauthorized"}."""

from fastapi import FastAPI, Response, Cookie
from models import User
from pydantic import BaseModel

app = FastAPI()
users = {}




@app.post("/login")
def login(user: User, response: Response):
    if user:
        token = "abc123xyz456"
        response.set_cookie(key="session_token", value=token, httponly=True)
        users[token] = user
        return {"Authenticated": True}

    return {"Error": "Проверьте правильность введенных данных!"}


@app.get("/user")
def get_user(session_token=Cookie()):
    user = users.get(session_token)
    if user:
        return {"user": users[session_token]}
