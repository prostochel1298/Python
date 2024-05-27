'''Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до 
величины «end» включительно. Если пользователь задаст первое число большее чем второе, 
просто поменяйте их местами.'''

def sum_range(start, end):
    n = start
    res = 0
    if start>end:
        for i in range(start-end+1):
            res+=n
            n-=1
    else: 
        for i in range(end-start+1):
            res+=n
            n+=1
    return res
print(sum_range(6,2))


     

