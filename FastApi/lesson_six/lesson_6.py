"""Чтобы создать асинхронный обработчик маршрута в FastAPI, мы используем синтаксис `async def`.
Асинхронный обработчик маршрута может содержать выражения `await`, указывающие точки, в которых функция может приостановить выполнение других задач,
пока она ожидает завершения асинхронной операции, такой как запрос к базе данных или HTTP-запрос.

Асинхронные обработчики маршрутов особенно полезны для обработки задач, связанных с вводом-выводом (I-O Bound), таких как выполнение сетевых запросов,
чтение и запись файлов или выполнение запросов к базе данных.
Вместо последовательного ожидания завершения каждой операции ввода-вывода асинхронные обработчики маршрутов могут инициировать несколько операций ввода-вывода одновременно,
позволяя приложению выполнять другие задачи в ожидании завершения операций ввода-вывода.""" 



"""FastAPI также поддерживает фоновые задачи, которые представляют собой функции, выполняемые после отправки ответа клиенту.
Фоновые задачи полезны для обработки задач, которые не должны блокировать основной цикл запроса-ответа, 
таких как отправка электронных писем, обновление аналитики или выполнение дополнительной неблокирующей обработки.
Чтобы использовать фоновые задачи в FastAPI, 
вы можете определить функцию фоновой задачи (с использованием класса BackgroundTasks) и включить ее в качестве параметра в обработчик маршрута.""" 

from fastapi import BackgroundTasks, FastAPI


app = FastAPI() 


def write_notification(email:str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content) 


@app.get("/send-notification/{email}")
async def send_notification(email: str, background_task: BackgroundTasks):
    background_task.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"} 


"""В практике более удобной, гибкой и функциональной для формирования и управления фоновыми задачами является библиотека Celery"""