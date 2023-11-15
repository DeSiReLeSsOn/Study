"""Создайте класс Human.

Определите для него два статических поля: default_name и default_age.

Создайте метод __init__(), который помимо self принимает еще два параметра: name и age.
Для этих параметров задайте значения по умолчанию,
используя свойства default_name и default_age. В методе __init__() определите четыре свойства:
Публичные - name и age. Приватные - money и house.

Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.

Реализуйте справочный статический метод default_info(),
который будет выводить статические поля default_name и default_age.

Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома:
уменьшать количество денег на счету и присваивать ссылку на только что купленный дом.
В качестве аргументов данный метод принимает объект дома и его цену.

Реализуйте метод earn_money(), увеличивающий значение свойства money.

Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки,
и совершать сделку.
Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода:
ссылка на дом и размер скидки"""

class Human:
    default_name = 'Unknown'
    default_age = 0

    def __init__(self, name= default_name, age=default_age, money=0, house=''):
        self.name = name
        self.age = age
        self._money = money
        self._house = house


    def info(self):
        return f'Name: {self.name}, Age: {self.age},Money: {self._money}, House: {self._house}'


    @staticmethod
    def default_info():
        return default_name, default_age


    def _make_deal(self, house, price):
        self.price = price
        if self._money >= self.price:
            self._money = self._money - self.price
            self._house = house
            print('Great job, deal completed!')
        else:
            print("Not enough money for deal")


    def earn_money(self, amount):
        self._money += amount


    def buy_house(self, house,  discount=0):
        price = house.price - discount
        if self._money >= self.price:
            self._money = self._money - self.price
            print('Great job, deal completed!')
        else:
            print("Not enough money for deal")


"""Задание. Часть 2. Класс House
Создайте класс House
 
Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price. 
Свои начальные значения они получают из параметров метода __init__()
 
Создайте метод final_price(), 
который принимает в качестве параметра размер скидки и возвращает цену с учетом данной скидки."""


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount=0):
        price = self._price - discount


"""Задание. Часть 3. Класс SmallHouse
Создайте класс SmallHouse, унаследовав его функционал от класса House
 
Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2"""


class SmallHouse(House):
    def __init__(self, area, price):
        super().__init__(area, price)
        self._area = '40м2'
        self._price = price

