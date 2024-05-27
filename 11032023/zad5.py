print("Вам пердстоит ввести два числа, где первое число будет меньше второго")
number1 = int(input("введите первое число: "))
number2 = int(input("введите второе число: "))
sp = []
a = number1
while a <= number2:
    sp.append(a)
    a+=1
b = 0
res = []
while b <= len(sp)-1:
    if sp[b]%2!=0:
        res.append(sp[b])
    b+=1
print(sum(res))