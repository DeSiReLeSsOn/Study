"""1. Объявите класс Calendar для хранения даты: день, месяц, год. Определите свойства для записи и считывания этой информации из этого класса. 
(Дополнение: используя __slots__ разрешите использовать только строго определенные локальные свойства в экземплярах класса).
"""





class Calendar:
    __slots__ = ['day', 'month', 'year']
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def set_day(self, day):
        self.day = day
    def get_day(self):
        return self.day
    def set_month(self, month):
        self.month = month
    def get_month(self):
        return self.month
    def set_year(self, year):
        self.year = year
    def get_year(self):
        return self.year
    

cl = Calendar(14, 11, 2022)


"""
2. Объявите класс Rectangle, хранящий координаты верхней левой и правой нижней точек. 
Создайте дескрипторы для записи и считывания этих значений в классе (атрибуты с данными координат должны быть приватными).""" 


class desc:
    def __set_name__(self, owner, name):
        self.name = ' ' + name 

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]
 
    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value 


class Rectangle:
    x = desc()
    y = desc()

    def __init__(self, x, y):
        self._x = x
        self._y = y 
    
    @classmethod
    def verify_coords(cls, coords):
        if type(coords) != int:
            raise TypeError('Координаты должны быть целым числом')


rec = Rectangle(1,4)
print(rec.__dict__)
