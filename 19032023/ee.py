cena = input("Введите цену товара через пробел: ")
prom = input("Введите промокод")
a= cena.split(" ")
num = list(map(int,a))
print(num[1])