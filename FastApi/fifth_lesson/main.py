"""Помимо параметров запроса, FastAPI также поддерживает параметры пути, которые являются частями URL-адреса, 
используемого для идентификации ресурсов, о чем мы упоминали ранее (`{параметр}`).
В дополнение можно отметить, что к параметрам пути можно добавить метаданные, задать им кастомный порядок, 
а также быстро провалидировать числовые данные (можете прочитать про импорт класса Path из fastapi).

Кроме того, вы можете передавать данные через тело запроса, используя (обычно) запросы POST и PUT для создания или обновления ресурсов.

Когда вам необходимо отправить данные из клиента (допустим, браузера, заполнив логин/пароль или отправив HTML-форму) в ваш API,
 вы отправляете их как тело запроса.

Тело запроса - это данные, отправляемые клиентом в ваш API. Тело ответа - это данные, которые ваш API отправляет клиенту.
Чтобы объявить тело запроса, необходимо использовать модели Pydantic. 

Чтобы добавить параметр к вашему обработчику, объявите его также,
 как вы объявляли параметры пути или параметры запроса и укажите созданную модель в качестве типа параметра, в примере Item:""" 

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item 


"""Union используется для объединения типов (создания более сложного типа).
В данном случае мы говорим, что тип у description и tax может быть либо строкой, либо None,
а также говорим, что параметр не обязателен (= None) - задаём значение по-умолчанию.""" 



"""FastAPI позволяет вам использовать как параметры пути, так и параметры запроса в одном и том же маршруте.
Такая гибкость позволяет разрабатывать API-интерфейсы,
которые обрабатывают широкий спектр запросов и сценариев обработки данных.""" 

@app.get("/users/{user_id}")
def read_user(user_id: int, is_admin: bool = False):
    return {"user_id": user_id, "is_admin": is_admin} 
    """В этом примере маршрут `/users/{user_id}` принимает параметр пути `user_id` и необязательный параметр запроса `is_admin`.
    Параметр `is_admin` по умолчанию имеет значение `False`, если он не указан в запросе.""" 


"""Path-параметры указывается в маршруте в фигурных скобках {}, а потом в обработчике маршрута:""" 

@app.get("/{some_param}")

async def func_with_path_param(some_param: type):
    pass 

# или прописываем явно: 
from typing import Annotated 
from pathlib import Path 

@app.get("/{some_param}")

async def func_with_path_param(some_param: Annotated[type, Path()]):
    pass 


"""Body-параметры представлены в виде Pydantic-моделей и указываются в виде параметра обработчика маршрута 
с типом соответствующего класса модели 
(о чем рассказывал осьранее):""" 
class User:
    pass

@app.post("/")

async def func_with_body_param(user: User): 
    pass


#или прописываем явно: 
class Body:
    pass
@app.post("/")

async def func_with_body_param(user: Annotated[User, Body()]):
    pass 


"""Query-параметры представлены просто в виде параметров обработчика маршрута (объявлены не двумя предыдущими способами):"""



@app.get("/")

async def func_with_body_param(query_param: type):
    pass 


#или указываем явно: 
class Query:
    pass 
@app.get("/")

async def func_with_body_param(query_param: Annotated[type, Query()]):
    pass 