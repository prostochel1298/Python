class TriangleChecker():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def is_trangle(self):
        if self.a == 0 or self.b == 0 or self.c == 0:
            print("Жаль, но из этого треугольник не сделать")
        elif isinstance(self.a,(bool,str)):
            print("Нужно вводить только числа!")
        elif isinstance(self.b,(bool,str)):
            print("Нужно вводить только числа!")
        elif isinstance(self.c,(bool,str)):
            print("Нужно вводить только числа!")
        elif self.a <0 or self.b<0 or self.c < 0:
            print("С отрицательными числами ничего не выйдет!")
        else:
            print("Ура, можно построить треугольник!")

Tre1=TriangleChecker(12,18,20)
Tre2=TriangleChecker("два",12,88)
Tre3=TriangleChecker(-77,33,76)
Tre4=TriangleChecker(0,22,77)

Tre1.is_trangle()
Tre2.is_trangle()
Tre3.is_trangle()
Tre4.is_trangle()



            
