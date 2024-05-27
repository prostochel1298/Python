'''Напишите программу, выводящую ряд Фибонначи.'''

num1=0
num2=1
fib=[]
fib.append(num1)
fib.append(num2)
for i in range(5):
    num3 = num1 + num2
    num1=num2
    num2=num3
    fib.append(num3)
print(fib)
    
    