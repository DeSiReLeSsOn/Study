"""Паттерн Прототип позволяет создавать объекты на основе уже существующего объекта-прототипа. 
Это позволяет избежать сложных операций создания объектов и улучшить производительность."""

import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj

class Car:
    def __init__(self):
        self.make = "Default"
        self.model = "Default"
        self.year = "Default"

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

car = Car()
prototype = Prototype()
prototype.register_object("Car", car)

# Клонирование объекта
car1 = prototype.clone("Car")
print(car1)

car2 = prototype.clone("Car", make="Toyota", model="Corolla", year=2021)
print(car2)

"""1. `Prototype` - класс, который содержит методы для регистрации, удаления и клонирования объектов.
2. `Car` - класс, объекты которого мы будем клонировать.
3. Мы создаем экземпляр `Car`, регистрируем его как прототип и клонируем его для создания новых объектов `car1` и `car2`.
4. Метод `clone` принимает имя объекта и атрибуты для обновления нового клонированного объекта.
5. Метод `__str__` переопределен для удобного вывода информации о машине."""