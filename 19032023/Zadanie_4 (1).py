'''У пользователя запрашиватся слово, буквы которого затем должны заменяться числами, соответствующими
порядкогому номеру данной буквы в алфавите. Напишите код данной программы.'''
b = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
g = []
for i in b:
    g.append(i)
b = b.split()
a = input("Введите числа через пробел: ")
d=[]
for i in a:
    try:
        d.append(int(i))
    except ValueError:
        continue
o = []
c = list(map(lambda x:o.append(g[x-1]),d))
k = " "
for i in o:
    k+=i
print(k)