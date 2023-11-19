class DataBase:
    """Простейшая реализация singleton.
    Чтобы всегда существовал только один экземпляр класса , а при попытке создать второй ....N,
    на новый созданный экземпляр,  ставилась ссылка уже созданного ранее.
    У данной реализации нет метода который бы не давал заменить атрибуты,
    поэтому атрибуты user, password, port всегда будут менятся при создании нового эеземпляра !"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.password} , {self.port}')

    def close(self):
        print(f'Закрытие соединения с БД')

    def read(self):
        return 'Data from DB'

    def write(self, data):
        print(f'Запись в БД {data}')



db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '4567', 40)
print(id(db), id(db2)) #на данном этапе видно, что двух экземпляров одиннаковвый id


db.connect()
db2.connect() # при создании данного экземпляра, перезаписались все атрибуты