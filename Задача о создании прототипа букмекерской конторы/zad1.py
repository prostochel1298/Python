from statistics import *

def zarplata():
    zp = list()
    vvod_zarplata = int(input("Введите зарплаты, стоп - 1: "))
    while vvod_zarplata != 1:
        zp.append(vvod_zarplata)
        vvod_zarplata = int(input("Введите зарплаты, стоп - 1: "))
    if variance(zp) > 125:
        zp2 = list()
        for i in zp:
            i = mean(zp)
            zp2.append(i)
        print("Слишком большая зарплата у всех, уравниваем ее",zp2) 
    else:
        for i in zp:
            i = i*2
        print("слишком маленька зп",zp)
     
zarplata()
