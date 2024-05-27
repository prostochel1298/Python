engl1 = {("A","E","I","O","U","L","N","S","T","R"):1}
engl2 = {("D", "G"):2}
engl3 = {("B", "C", "M", "P"):3}
engl4 = {("F", "H", "V", "W", "Y"):4}
engl5 = {"K":5}
engl6 = {("J", "X"):8}
engl7 = {("Q", "Z"):10}

slovo = input("Введите слово на англйском: ")
sp1 = list()
for i in slovo:
    sp1.append(i)
summ = 0
for i in sp1:
    if i in engl1.keys():
        summ+=1
    elif i in engl2.keys():
        summ+=2
    elif i in engl3.keys():
        summ+=3
    elif i in engl4.keys():
        summ+=4
    elif i in engl5.keys():
        summ+=5
    elif i in engl6.keys():
        summ+=8
    elif i in engl7.keys():
        summ+=10
print("Сумма набранного слова равна: ", summ)


