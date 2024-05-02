"""Реализуйте защищенную базовой аутентификацией конечную точку FastAPI `/login`, которая принимает запросы GET.

1. Конечная точка должна аутентифицировать пользователя на основе предоставленных учетных данных.

2. Используйте зависимость, чтобы проверить правильность имени пользователя и пароля.

3. Если учетные данные неверны, верните сообщение HTTPException с кодом состояния 401 (то же самое возвращается, если учетные данные не предоставлены).

4. Если данные верны, верните секретное сообщение "You got my secret, welcome"

5. Попробуйте сначала авторизоваться с неправильными данными, а потом введите корректные данные. 
Для получения такой возможности (повторно авторизоваться) изучите информацию про необходимость добавления заголовка WWW-Authenticate чтобы браузер снова отображал приглашение для входа в систему."""


from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials 

app = FastAPI()
security = HTTPBasic()


class User(BaseModel):
    username: str
    password: str


USER_DATA = [User(**{"username": "user1", "password": "pass1"}), User(**{"username": "user2", "password": "pass2"})]


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_fake_db(credentials.username)

    if user is None and user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No active account or invalid credentials!")
    return user 



def get_user_from_fake_db(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user 
        return None
    
@app.get("/login/")
def get_resource(user: User = Depends(authenticate_user)):
    return {"message": "You have access to the protected resource!", "user_info": user}


