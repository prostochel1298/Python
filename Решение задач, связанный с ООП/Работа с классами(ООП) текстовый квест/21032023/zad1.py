class Rome():
    def __init__(self,translate):
        self.translate = translate
    def number_rome(self):
        a = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}
        b = len(self.translate)
        if b == 1:
            print(a[int(self.translate)])
        else:
            if int(self.translate) % 10 == 0:
                if int(self.translate) == 10:
                    print(a[int(self.translate)])
                else:
                    print(a[10]*2)
            else:
                print(a[10]+a[int(self.translate)%10])
        

Num = Rome(input("Введите число: "))
Num.number_rome()
