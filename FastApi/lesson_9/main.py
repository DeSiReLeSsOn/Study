"""Ваша задача - создать приложение FastAPI, которое демонстрирует, как работать с заголовками запросов. 
Выполните следующие действия, чтобы выполнить задачу:

1. Создайте конечную точку в `/headers`, которая принимает запросы GET.

2. В конечной точке `/headers` извлеките следующие заголовки из входящего запроса:

   a) "User-agent": строка пользовательского агента браузера клиента или пользовательского агента пользователя.

   б) "Accept-Language": предпочтительный язык клиента для согласования содержимого.

3. Верните ответ в формате JSON, содержащий извлеченные заголовки и их значения.

Пример:

GET-запрос к `/headers` со следующими заголовками:

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
Accept-Language: en-US,en;q=0.9,es;q=0.8
Ответ JSON должен быть таким:

{
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8"
}
4. Реализуйте обработку ошибок, чтобы вернуть соответствующий ответ с кодом состояния 400 (неверный запрос), 
если необходимые заголовки отсутствуют."""


from fastapi import FastAPI, Header, Response, Request

app = FastAPI() 

@app.get("/headers")
def root(request: Request):
    user_agent = request.headers.get("User-Agent")
    accept_language = request.headers.get("Accept-Language")
    return {"User-Agent": user_agent, "Accept-Language": accept_language}