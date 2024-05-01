#БАЗОВАЯ АУНТЕНТИФИКАЦИЯ....

#Шаг 1: Импорт зависимостей    
from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials

#Шаг 2: Создайте приложение FastAPI и экземпляр HTTPBasic
app = FastAPI()
security = HTTPBasic()


#Шаг 3: Создайте модель пользователя
class User(BaseModel):
    username: str
    password: str

#добавим симуляцию базы данных в виде массива объектов юзеров
USER_DATA = [User(**{"username": "user_1", "password": "pass1"}, User(**{"username": "user_2", "password": "pass2"}))]


#Шаг 4: Определите функцию аутентификации
def authenticate_user(credentials: HTTPBasicCredentials= Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    return user 


#Шаг 5: Задайте логику получения информации о пользователе и его пароле

@app.get("/protected_resource/")
def get_protected_resource(user: User = Depends(authenticate_user)):
    return {"message": "You have access to the protected resource!", "user_info": user}

"""В приведенном выше коде мы сначала импортируем необходимые зависимости, включая `FastAPI`, `HTTPBasic` и `HTTPBasicCredentials`. 
Затем мы создаем экземпляр `HTTPBasic` для использования для аутентификации. 
Мы определяем функцию `authenticate_user`, которая принимает `HTTPBasicCredentials` в качестве параметра, полученного из запроса. 
Эта функция проверяет учетные данные пользователя по базе данных и выдает ошибку HTTP 401 Unauthorized, если они недействительны.
Наконец, мы защищаем нашу конечную точку, добавляя функцию `authenticate_user` в качестве зависимости. 
Когда клиент отправляет запрос к конечной точке `/protected_resource/`, 
FastAPI сначала запустит функцию `authenticate_user` для проверки учетных данных пользователя, прежде чем выполнять основную функцию конечной точки."""