class Triangle:
    def __init__(self):
        self.lenght = 5
        self.hight = 10
    def ploshad(self):
        print("Площадь треугольник равна: ",(self.hight/2)*self.lenght)
class Quadrat:
    def __init__(self):
        self.lenght = 8
    def ploshad(self):
        print("Площадь квадрата равна:",self.lenght**2)
tre = Triangle()
qua = Quadrat()
tre.ploshad()
qua.ploshad()
    