class Figure:
    def __init__(self,name):
        self.name = name
    def info(self):
        print("Я двумерная фигура")
    def ploshad(self):
        pass

class Square(Figure):
    def __init__(self, name,a):
        self.a=a
        super().__init__(name)
    def info(self):
        print("Я двумерная фигура с одинаковыми сторонами и углами")
    def ploshad(self):
        print("Площадь равна:",self.a**2)
        
class Tre(Figure):
    def __init__(self, name,a,h):
        self.a = a
        self.h = h
        super().__init__(name)
    def info(self):
        print("Я двумерная фигура с тремя сторонами и тремя углами")
    def ploshad(self):
        print("Площадь фигуры равна:",((self.h/2)*self.a))
a = Figure("Фигура")
a.info()
b = Square("Квадрат",6)
b.info()
b.ploshad()
c = Tre("Треугольник",5,9)
c.info()
c.ploshad()
