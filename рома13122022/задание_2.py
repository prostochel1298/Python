'''Используя операции индексирования и среза выведите на экран первый и 
третий элементы кортежа (1, 2, 3, 4, 5), а также срез кортежа из первых трех элементов. 
Реализуйте вывод двумя способами: используя только положительные и только отрицательные индексы.'''

a = (1,2,3,4,5,6,17,10)
# с 1 по 5 (через плюс и минус)
# до 4 (через плюс  минус)
print(a[:5])
print(a[:-3])

print(a[:4])
print(a[:-4])