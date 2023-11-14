"""На предыдущем модуле мы с вами рассмотрели создание объектов-свойств и видели, 
что для определения нескольких однотипных таких объектов приходится дублировать программный код, что не очень хорошо. 
Чтобы этого избежать можно воспользоваться механизмом дескрипторов и сейчас вы узнаете что это такое.

В самом простом случае дескриптор – это класс, в котором определены следующие специальные методы:""" 

class CoordValue:
    def __get__(self, instance, owner):
        return self.__value
 
    def __set__(self, instance, value):
        self.__value = value
 
    def __delete__(self, obj):
        del self.__value 

    #get – это геттер, set – сеттер, а delete – вызывается при удалении свойства дескриптора.  


class Point:
    coordX = CoordValue()
    coordY = CoordValue()
 
    def __init__(self, x = 0, y = 0):
        self.coordX = x
        self.coordY = y

 
"""Здесь параметр instance ссылается на экземпляр класса Point, для которого был вызван метод. 
И через него, используя коллекцию __dict__ мы делаем обработку локальных свойств: возвращаем их или устанавливаем. 
А, чтобы знать имя локального свойства, здесь был добавлен конструктор с параметром name – имя свойства. 
И мы его сохраняем в экземпляре объекта-дескриптора в приватной переменной __name"""
class CoordValue:
    def __init__(self, name):
        self.__name = name
 
    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]
 
    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value 


"""Далее, в самом классе Point сделаем такие вызовы:""" 

coordX = CoordValue("coordX")
coordY = CoordValue("coordY") 


"""при запуске программы, мы видим разные значения координат для разных экземпляров классов:""" 


pt = Point(1, 2)
pt2 = Point(10, 20)
print( pt.coordX, pt.coordY )
print( pt2.coordX, pt2.coordY )
