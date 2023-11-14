"""Инкапсуляция:

Напишите класс «Стол» с «полной инкапсуляцией», доступ к атрибутам которого и изменение данных реализуются через вызовы методов гет и сет.
В объектно-ориентированном программировании принято имена методов для извлечения данных начинать со слова get (взять), а имена методов,
в которых свойствам присваиваются значения, – со слова set (установить). Например, getField, setField.
""" 


class Table:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        
    def get_x(self,x):
        return self.__x 
    
    def get_y(self,y):
        return self.__y
    


"""
Напишите класс «Авто» с «полной инкапсуляцией», с доступом через аннотацию свойств и проверкой условий правильности вводимых данных.""" 


class Auto:
    def __init__(self, model: str, year: int, price: float, mileage: float):
        self.__model = model
        self.__year = year 
        self.__price = price
        self.__mileage = mileage 


    @property
    def show_info(self):
        return self.model,self.year,self.price
    
    @property
    def mileage(self):
        return self.__mileage
    
    @mileage.setter
    def mileage(self, value):
        if value > 0:
            self.__mileage = value 
        else:
            raise ValueError("Mileage must be a positive number")
        