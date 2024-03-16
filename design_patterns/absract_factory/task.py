"""Мы помогаем дизайнерам делать различные кнопки в пользовательских интерфейсах.
У нас есть 2 платформы: Mac OS и Windows OS
У нас так же есть 2 вида кнопок: CheckBox и PushButton

Задача:

Создать на основе абстрактной фабрики структуру создания кнопок.
Кнопки для Mac OS - белые, для Windows OS - синие.
Функция push() выводит 1 из 4х вариантов в зависимости от ОС и типа кнопки:

"На кнопку нажали, цвет белый"
"На кнопку нажали, цвет синий"
"Галочка поставлена, цвет белый"
"Галочка поставлена, цвет синий"
"""


import abc
class AbstractGUIFactory(metaclass=abc.ABCMeta):
    """Создаем абстрактный класс для типа ОС"""
    @abc.abstractmethod
    def create_checkbox(self):
        pass
    @abc.abstractmethod
    def create_button(self):
        pass
    
    
class AbstractButton(metaclass=abc.ABCMeta):
    """Создаем абстрактный класс для типа кнопки"""
    @abc.abstractmethod
    def push(self):
        pass
    
class PushButton(AbstractButton):
    """Инициализуем цвет и создаем метод push для типа кнопки button"""
    def __init__(self, color):
        self.color = color
    def push(self):
        print(f"На кнопку нажали, цвет {self.color}")
        
        
class CheckBox(AbstractButton):
    """Инициализуем цвет и создаем метод push для типа кнопки checkbox"""
    def __init__(self, color):
        self.color = color
    def push(self):
        print(f"Галочка поставлена, цвет {self.color}")
        

    
    

class MacFactory(AbstractGUIFactory):
    def create_checkbox(self):
        return CheckBox("белый")
    
    def create_button(self):
        return PushButton("белый")
    
    
class WinFactory(AbstractGUIFactory):
    def create_checkbox(self):
        return CheckBox("синий")
    
    def create_button(self):
        return PushButton("синий")