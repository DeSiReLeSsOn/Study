"""Задание :
 Создайте суперкласс «Персональные компьютеры» и на его основе подклассы: «Настольные ПК» и «Ноутбуки».
 В базовом классе определите общие свойства: размер памяти, диска, модель, CPU. А в производных классах уникальные свойства:

для настольных: монитор, клавиатура, мышь, их габариты; и метод для вывода этой информации в консоль;
для ноутбуков: габариты, диагональ экрана; и метод для вывода этой информации в консоль.""" 



class Pc:
    disk_size = 1024
    ram_size = 3000
    model = 'ABM'  


class Static_pc(Pc):
    monitor = 'Full_HD'
    keyboard = 'DeTech' 
    dimensions = '140cm/80cm'

    def show_characteristics(self):
        print(self.monitor, self.keyboard, self.dimensions) 



class LapTop(Pc):
    dimensions = '30cm/50cm' 
    monitor_size = '15d' 


    def show_characteristics(self):
        print(self.dimensions, self.monitor_size)  


pc = Pc() 
s_pc = Static_pc()
l_p = LapTop()
 

print(s_pc.show_characteristics())
print(l_p.show_characteristics())