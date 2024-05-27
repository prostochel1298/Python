
class Train():
    def __init__(self,dest,number,times):
        self.dest=dest
        self.number=number
        self.times=times
    
    
    def info(self):
        print("Пункт назначения поезда: ", self.dest)
        print("Номер поезда: ",self.number)
        print("Время отпарвления:", self.times)
  
        
t1=Train("Новосибирск",25,"17:15") 
t2=Train("Кемерово",44,"20:00")
t3=Train("Кемерово",21,"13:00")
t4=Train("Красноярск",83,"23:30")
t5=Train("Томск",31,"14:20")

def train_info():
   num =  int(input("Введите номер нужного Вам поезда(0-отмена): "))
   while num != 0:
    if num == 25:
        t1.info()
    elif num == 44:
        t2.info()
    elif num == 21:
        t3.info()
    elif num == 83:
        t4.info()
    elif num == 31:
        t5.info()
    else:
        print("Такого поезда не существует!")
    num =  int(input("Введите номер нужного Вам поезда(0-отмена): "))

def sortirovka1():
    g=list()
    n1=t1.__dict__.values()
    n2=t2.__dict__.values()
    n3=t3.__dict__.values()
    n4=t4.__dict__.values()
    n5=t5.__dict__.values()
    for i in n1:
        g.append(i)
    for i in n2:
        g.append(i)
    for i in n3:
        g.append(i)
    for i in n4:
        g.append(i)
    for i in n5:
        g.append(i)

    s = list()

    for b in g:
        if isinstance(b,str):
            s.append(b)

    s.sort()
    del s[:5]
    print(s)


def sortirovka2():

    tt1=vars(t1)
    tt2=vars(t2)
    tt3=vars(t3)
    tt4=vars(t4)
    tt5=vars(t5)

    ds = [tt1,tt2,tt3,tt4,tt5]
    d = {}
    for k in tt1.keys():
        d[k] = list(d[k] for d in ds)


    for l in d.values():
        l.sort()

    print(d)
sortirovka2()

