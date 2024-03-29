"""Задача: реализовать шаблон композитного проектирования в Python.

Рассмотрим пример файловой системы, состоящей из файлов и каталогов. Каждый файл и каталог является компонентом древовидной структуры файловой системы. Каталог может содержать другие каталоги и файлы, а файл не может содержать никаких других компонентов.
а. Определите базовый класс компонента с именем `Component` с абстрактным методом с именем `display()`.
б. Реализуйте класс листового компонента с именем `File`, который представляет файл в файловой системе. Он должен наследоваться от класса Component и реализовывать метод display() для отображения имени файла.
в. Реализуйте составной компонентный класс с именем `Directory`, который представляет каталог в файловой системе. Он должен наследоваться от класса Component и реализовывать метод display() для отображения имени каталога. Он также должен иметь список дочерних компонентов, которые могут быть файлами или другими каталогами.
д. Определите клиентский класс с именем `Client`, который принимает объект Component в качестве входных данных и использует метод `display()` для отображения имени компонента."""



from abc import ABC, abstractmethod
    
class Component(ABC):
    @abstractmethod
    def display(self, indent=""):
        pass

class File(Component):
    def __init__(self, name: str):
        self.name = name

    def display(self, indent=""):
        print(indent + "|- " + self.name)

    def __str__(self):
        return self.name

class Directory(Component):
    def __init__(self, dir_name: str):
        self.dir_name = dir_name
        self.dir_list = list()

    def display(self, indent=""):
        print(indent  + self.dir_name)
        for child in self.dir_list:
            child.display(indent + "|  ")

    def add_child(self, file):
        self.dir_list.append(file)

class Client:
    def __init__(self, component):
        self.component = component

    def display(self):
        self.component.display()

    def __str__(self):
        return self.component.display()

    

"""
Пример теста
root = Directory("root")
file1 = File("file1")
file2 = File("file2")
dir1 = Directory("dir1")
file3 = File("file3")
file4 = File("file4")
dir2 = Directory("dir2")
file5 = File("file5")
file6 = File("file6")
dir3 = Directory("dir3")
file7 = File("file7")
file8 = File("file8")
root.add_child(file1)
root.add_child(file2)
root.add_child(dir1)
dir1.add_child(file3)
dir1.add_child(file4)
dir1.add_child(dir2)
dir2.add_child(file5)
dir2.add_child(file6)
root.add_child(dir3)
dir3.add_child(file7)
dir3.add_child(file8)
client = Client(root)
client.display()
"""