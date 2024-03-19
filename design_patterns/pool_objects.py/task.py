"""Задача!

Возьмем за основу задачу о подключениях к базе данных. 
Вам нужно на примере пула объектов создать класс DbPool, который является менеджером DbConnection. 
Нужно ограничить количество подключений до 10. 

Самое главное - это создать функцию acquire(), которая будет выдавать строку 
'Доступы выданы, осталось подключений: n', где n - количество объектов DbConnection в пуле, 
когда подключений достаточно (не более 10), и строку 'no resources', 
когда количество подключений превышает 10. """


class DbPool:
    def __init__(self, size=10):
        self._reusable = [DbConnection() for _ in range(size)]
        
    def acquire(self):
        if len(self._reusable) >= 1:
            for _ in self._reusable:
                self._reusable.pop()
                return f"Доступы выданы, осталось подключений: {len(self._reusable)}"
        else:
            
            return 'no resources'

class DbConnection:
    pass