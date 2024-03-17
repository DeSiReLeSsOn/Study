"""Мы банк и подготавливаем данные для принятия решения по клиенту: одобрить или отказать по кредиту. 
Для этого нам нужно сделать:

запрос в БКИ
звонок на работу
оценить его недвижимость
После этого мы упаковываем полученные данные и отправляем в скоринг для принятия решения.

Задание:

Создать на основе паттерна "Строитель" структуру таких проверок."""

import abc

class Builder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _nbki_request(self):
        pass

    @abc.abstractmethod
    def _job_call(self):
        pass

    @abc.abstractmethod
    def _property_check(self):
        pass

class Product:
    def __init__(self):
        self.result = [] # ['БКИ проверен', "На работу позвонили", "Недвижимость есть"]

class ConcreteBuilder(Builder):
    def _nbki_request(self):
        self.product.result.append('БКИ проверен')
        return self

    
    def _job_call(self):
        self.product.result.append("На работу позвонили")
        return self

   
    def _property_check(self):
        self.product.result.append("Недвижимость есть")
        return self

class Director:
    def construct(self, builder):
        builder._nbki_request()
        builder._job_call()
        builder._property_check()
        return builder.product
        