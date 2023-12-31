"""Термин полиморфизм буквально означает наличие нескольких форм.
В контексте объектно-ориентированного программирования, полиморфизм означает способность объекта вести себя по-разному.

Полиморфизм в программировании реализуется через перегрузку метода, либо через его переопределение.""" 

# создаем класс Car
class Car:  
   def start(self, a, b=None):
        if b is not None:
            print (a + b)
        else:
            print (a) 

"""В скрипте выше, если метод start() вызывается передачей одного аргумента, параметр будет выведен на экран.
Однако, если мы передадим 2 аргумента методу start(), он внесет оба аргумента и выведет результат суммы."""  

#передадим один аргумент
car_a = Car()  
print(car_a.start(10)) # вывод 10 

# а теперь передадим 2 аргумента
print(car_a.start(10, 20)) # вывод 30 


"""Переопределение метода относится к наличию метода с одинаковым названием в дочернем и родительском классах.
Определение метода отличается в родительском и дочернем классах, но название остается тем же.
Давайте посмотрим на простой пример переопределения метода в Python.""" 


# создание класса Vehicle
class Vehicle:  
    def print_details(self):
        print("Это родительский метод из класса Vehicle")

# создание класса, который наследует Vehicle
class Car(Vehicle):  
    def print_details(self):
        print("Это дочерний метод из класса Car")

# создание класса Cycle, который наследует Vehicle
class Cycle(Vehicle):  
    def print_details(self):
        print("Это дочерний метод из класса Cycle")  

"""классы Cycle и Car наследуют класс Vehicle. Класс Vehicle содержит метод print_details(), который переопределен дочерним классом.
Теперь, если вы вызовите метод print_details(), выдача будет зависеть от объекта, через который вызывается метод. """ 

car_a = Vehicle()  
print(car_a. print_details()) #Это родительский метод из класса Vehicle

car_b = Car()  
print(car_b.print_details()) #Это дочерний метод из класса Car

car_c = Cycle()  
print(car_c.print_details()) # Это дочерний метод из класса Cycle
