"""Задание: Обьъявите класс TriangleChecker, обьъекты которго можно создавать командой tr = TriangleChecker(a, b, c)
a, b, c - длины сторон треугольника . В классе необходимо объявить метод is_triangle() который бы возвращял следующие коды
1- если хотя бы одна сторона не число(float, int)
2- указанные числа a,b,c не могут являтся длинами сторон треугольника
3- стороны a,b,c образуют треугольник"""

class TriangleChecker:


    def __init__(self, x, y, c):
        self.x = x
        self.y = y 
        self.c = c 

    def is_triangle(self, x, y, c):
        if type(x,y,c) != float and type(x,y,c) != int:
            return 1
        elif x <= 0 and y <= 0 and c <=0:
            return 2
        else:
            return 3



        