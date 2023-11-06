"""Расширьте существующее приложение FastAPI, создав конечную точку POST, которая позволяет пользователям отправлять отзывы.
 Конечная точка должна принимать данные JSON, содержащие имя пользователя и сообщение обратной связи.

1. Определите Pydantic модель с именем "Feedback" (обратная связь) со следующими полями:
   - `name` (str)
   - `message` (str)

2. Создайте новый маршрут публикации "/feedback", который принимает данные JSON в соответствии с моделью `Feedback`.

3. Реализуйте функцию для обработки входящих данных обратной связи и ответа сообщением об успешном завершении.

4. Сохраните данные обратной связи в списке или хранилище данных, чтобы отслеживать все полученные отзывы.

Пример:
Запрос JSON:

{
    "name": "Alice",
    "message": "Great course! I'm learning a lot."
}
Ответ JSON:

{
    "message": "Feedback received. Thank you, Alice!"
}
Пожалуйста, протестируйте свою реализацию с помощью таких инструментов,
 как "curl", Postman или любой другой клиент API, чтобы отправить отзыв и проверить ответ"""

from model import Feedback 
from fastapi import FastAPI

app = FastAPI()  

lst = list()


@app.post("/feedback")
async def response_feedback(feedback: Feedback):
    lst.append({"name": feedback.name, "comments": feedback.message})
    return f"Feedback received. Thank you, {feedback.name}!"


@app.get("/comments")
async def show_feedback():
    return lst








