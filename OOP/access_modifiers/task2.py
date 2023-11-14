"""Написать класс стол который принимает параметры: высота, ширина, тип (круглый или квадратный)""" 

class Table:
    def __init__(self, height: int, width: int, type_table: str):
        self.height = int(height)
        self.width = int(width)
        self.type_table = type_table
        if self.type_table.lower() != 'rectangle' and self.type_table.lower() != 'round':
            raise ValueError("Wrong type")


"""написать класс «квадратный стол» на следующий основной класс «Стол».
И добавить в новый класс методы расчёта площади столешницы по соответствующим формулам.""" 


class Round_Table(Table):
    def __init__(self, height: int, width: int, type_table: str):
        super().__init__(height, width, type_table)
    def calculate_area(self):
        return 3.14 * self.width * self.height
    

class RectangleTable(Table):
    def __init__(self, height: int, width: int, type_table: str):
        super().__init__(height, width, type_table)
    def calculate_area(self):
        return self.width * self.height
    
    
tb = Table(123, 125, 'round')

tb2 = Round_Table(123, 125, 'round')


"""Написать один класс «Стол» включающим поле «форма столешницы» с методом «площадь столешницы»,
который вычисляет площадь в зависимости от выбранной формы."""

class Table2:
    def __init__(self, height: int, width: int, type_table: str):
        self.height = int(height)
        self.width = int(width)
        self.type_table = type_table
        if type_table.lower() == 'round':
            def calculate_area(self):
                return 3.14 * self.width * self.height
        elif type_table.lower() == 'rectangle':
            def calculate_area(self):
                return self.width * self.height




        
