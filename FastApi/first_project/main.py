from fastapi import FastAPI
from pydantic import BaseModel 
from models import User

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



@app.get("/users")
def user():

    second_user_data = {
        "id": 1,
        "name": "John Doe"
    }

    my_second_user: User = User(**second_user_data)
    return my_second_user