from random import*
sp  = []
spisok = input("Введите фамилии.'Cтоп - остановить': ")
while spisok != "стоп":
    sp.append(spisok)
    spisok = input("Введите фамилии.'Cтоп - остановить': ")
sp2 = []
number = 1
for i in sp:
    sp2.append(i+"-"+str(number))
    number+=1

sp3 = []
while len(sp3)<3:
    number2 = randint(1,len(sp2))
    if number2 not in sp3:
        sp3.append(number2)
print(sp3)
    
    


    


    


