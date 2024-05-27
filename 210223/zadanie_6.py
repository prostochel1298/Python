'''Напишите программу на Python для вывода числа с запятыми в качестве разделителей тысяч.'''

num = "1000000"
res=""
for i in range(len(num)):
    if i == 1 or i == 4:
        res += "."
    res+=num[i]
    
      
    
print(res)