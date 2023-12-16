from fastapi import FastAPI 
from fastapi.responses import FileResponse


"""FastAPI поддерживает различные методы HTTP, включая GET, POST, PUT, DELETE и другие, для обработки различных типов запросов.
Определив функции Python, оформленные соответствующими декораторами HTTP-методов, 
вы можете проинструктировать FastAPI о том, как обрабатывать запросы каждого типа.
POST - отправка новых данных на сервер.
GET - получение информации
PUT - вносит изменения в уже имеющуюся на сервере информацию. 
DELETE - удаление

В FastAPI можно также использовать операции:

@app.get()
@app.post()
@app.put()
@app.delete()

"""



app = FastAPI()

@app.get("/") 
async def root():
    return FileResponse("index.html")