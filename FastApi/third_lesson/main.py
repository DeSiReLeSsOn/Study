from fastapi import FastAPI
from pydantic import BaseModel 
from models import User

"""Ваша задача состоит в том, чтобы расширить существующее приложение FastAPI, добавив новую конечную точку POST, которая принимает данные JSON, представляющие пользователя, и возвращает те же данные с дополнительным полем, указывающим, является ли пользователь взрослым или нет.

1. Определите Pydantic модель с именем "Пользователь" ("User") со следующими полями:

   - `name` (str)

   - `age` (int)

2. Создайте новый маршрут `/user`, который принимает запросы POST и принимает полезную нагрузку JSON, содержащую пользовательские данные, соответствующие модели `User`.

3. Реализуйте функцию для проверки того, является ли пользователь взрослым (возраст >= 18) или несовершеннолетним (возраст < 18).

4. Верните пользовательские данные вместе с дополнительным полем `is_adult` в ответе JSON, указывающим, является ли пользователь взрослым (True) или несовершеннолетним (False).

Пример:
Запрос в формате JSON:

{
    "name": "John Doe",
    "age": 25
}
Ответ в формате JSON:

{
    "name": "John Doe",
    "age": 25,
    "is_adult": true
}
Пожалуйста, протестируйте свою реализацию с помощью таких инструментов, как "curl", Postman или любой другой клиент API."""

app = FastAPI()

# пример роута (маршрута)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}  

# новый роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"} 


@app.post("/")
async def root(user: User):
    '''тут мы можем с переменной user, которая в себе содержит объект класса User с соответствующими полями (и указанными типами), делать любую логику
    - например, мы можем сохранить информацию в базу данных
    - или передать их в другую функцию
    - или другое'''
    print(f'Мы получили от юзера {user.username} такое сообщение: {user.message}') # тут мы просто выведем полученные данные на экран в отформатированном варианте
    return user # или можем вернуть обратно полученные данные, как символ того, что данные получили, или другая логика на ваш вкус 

user = User(name="John Doe", age=25)

@app.get("/users")
async def get_user():
    return user.dict()


@app.post("/user")
async def check_user():
    is_adult = True if user.age >= 18 else False 
    user_dict = user.dict() 
    user_dict['is_adult'] = is_adult
    return user_dict


    



#uvicorn main:app --reload  - запустить сервер гд main -имя приложения