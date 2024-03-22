"""Программа должна выводить строку "Вы подключились к базе данных", если подключение произведено первый раз. 
В остальных случаях - "Существует активное подключение"."""


class Singleton(type):
    _instance = None
    def __call__(cls):
        if cls._instance is None:
            cls._instance = super.__call__()
            print("Вы подключились к базе данных")
        else:
            print("Существует активное подключение")
            
        

class DbConnection(metaclass=Singleton):
    pass