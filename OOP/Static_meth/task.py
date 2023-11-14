"""Напишите программу, в которой пользователь вводит координаты x, y с клавиатуры, создается соответствующий экземпляр и он сохраняется в списке. Количество вводимых объектов N=5. Затем, вывести их атрибуты в консоль.""" 
class Coords:
    def __init__(self, x, y, c):
        self.x = x 
        self.y = y
        self.c = c
    
res = []
N = 5
for _ in range(N):
    x = int(input("Введите координату x: ")) 
    y = int(input("Введите координату y: "))
    c = int(input("Введите координату c: "))
    res.append(Coords(x,y,c))

for point in res:
    print(f'Координаты:{point.x}, {point.y}, {point.c}')


        