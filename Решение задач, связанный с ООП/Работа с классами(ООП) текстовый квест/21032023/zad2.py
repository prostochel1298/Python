class Govnoebanoe():
    def __init__(self,number):
        self.number = number
    def summa(self):
        lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for i in lst:
            for b in lst:
                if i+b == self.number:
                    print(lst.index(i),lst.index(b))

a = Govnoebanoe(int(input("Введи число: ")))
a.summa()