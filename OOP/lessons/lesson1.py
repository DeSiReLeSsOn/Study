class Point:
    """documentation"""
    color = 'red'
    circle = 2 


#вывести отдельный атрибут класса
print(Point.color)


#вывести все атрибуты класса 
print(Point.__dict__)


#создать экземпляр класса
a = Point()


#изменить атрибут класса,а так же присвоить значение(так же меняет этот атрибут во всех дочерних классах!)
Point.circle = 1

#изменить атрибут в дочернем экземпляре 
a.color = 'green'

#так же изменить атрибут можно с помощью встроенного метода setattr(первым аргументом принимает пространство имен ,вторым аргументов в виде строки атрибут который хотим изменить/создать ,третьим значение которое хотим установить)
setattr(Point, 'prop', 1)


#прочитать атрибут класса с помощью getattr(первый агрумент пространство имен,второй - атрибут который хотим прочитать, третьим то что будет выведенно если такого атрибута не существует)
getattr(Point,'a', False)  


#проверить существует ли атрибут , с помощью hasattr(первый аргумент пространство имен, второй аргумент- атрибут  )
hasattr(Point, 'circle')

#удалить атрибут класса
del Point.prop 


#так же удалить атрибут 
delattr(Point, 'prop')

#прочитать документацию 
print(Point.__doc__)

