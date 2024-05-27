lst = input("введите 8 чисел,для остановки напишите 'стоп': ")
b=[]
while lst != "стоп":
    b.append(lst)
    lst = input("введите числа,для остановки напишите 'стоп': ")

fuck=[]

def new_spisok():
    for i in b:
        if b.count(i) == 1:
            fuck.append(i)
    print(fuck)
            

new_spisok()

