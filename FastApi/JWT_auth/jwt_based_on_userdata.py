"""Иногда нужно быстро сделать аутентификацию, используя имя пользователя и пароль (например, при разработке внутри компании). 
Для этого можно использовать возможности FastAPI по работе с OAuth2: """


from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import jwt


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Секретный ключ для подписи и верификации токенов JWT
SECRET_KEY = "mysecretkey" # тут мы в реальной практике используем что-нибудь вроде команды Bash (Linux) 'openssl rand -hex 32', и храним очень защищенно
ALGORITHM = "HS256" # плюс в реальной жизни мы устанавливаем "время жизни" токена

# Пример информации из БД
USERS_DATA = [
    {"username": "admin", "password": "adminpass"}
] # в реальной БД мы храним только ХЭШИ паролей (можете прочитать про библиотеку, к примеру, 'passlib') + соль (известная только нам добавка к паролю)

class User(BaseModel):
    username: str
    password: str


# Функция для создания JWT токена
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM) # кодируем токен, передавая в него наш словарь с тем, что мы хотим там разместить

# Функция получения User'а по токену
def get_user_from_token(token: Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM) # декодируем токен
        return payload.get("sub") # тут мы идем в полезную нагрузку JWT-токена и возвращаем утверждение о юзере (subject); обычно там еще можно взять "iss" - issuer/эмитент, или "exp" - expiration time - время 'сгорания' и другое, что мы сами туда кладем 
    except jwt.ExpiredSignatureError:
        pass # тут какая-то логика ошибки истечения срока действия токена
    except jwt.InvalidTokenError:
        pass # тут какая-то логика обработки ошибки декодирования токен


# Функция для получения пользовательских данных на основе имени пользователя
def get_user(username: str):
    for user in USERS_DATA:
        if user.get("username") == username:
            return user
    return None


# роут для аутентификации; так делать не нужно, это для примера - более корректный пример в следующем уроке
@app.post("/login")
async def login(user_in: User): 
    for user in USERS_DATA:
        if user.get("username") == user_in.username and user.get("password") == user_in.password:
            return {"access_token": create_jwt_token({"sub": user_in.username}), "token_type": "bearer"}
    return {"error": "Invalid credentials"}


# защищенный роут для получения информации о пользователе
@app.get("/about_me")
async def about_me(current_user: str = Depends(get_user_from_token)):
    user = get_user(current_user)
    if user:
        return user
    return {"error": "User not found"}