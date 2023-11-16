""" Менеджер контекста(мк) - это специальная конструкция управления к ресурсу
базовый синтаксис мк- 
with <менеджер контекста> as <переменная>:
    список конструкция языка Python .

в менеджере контекста реализованны:
__enter__() - метод срабатывает в момент создания объекта менеджера контекста.
__exit__() - срабатывает в момент завершения работы менеджера контекста или возникновения исключения.
P.S не каждый обьект можно записывать в менеджер контекста
"""
import os

with open("myfile.txt", 'w') as file: # открывает file.txt  в режиме записи ,далее мы может обращатся к методу через переменную file
    file.write('smth interesting')
    file.write('nthg interesting')
    #между этими строками будет вызван метод __exit__() именуемы как close()
print('end')

with os.scandir("..") as entries: #функция модуля os.scandir() сканирует текущуюю папку и все содержимое записывается в переменную entries
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")