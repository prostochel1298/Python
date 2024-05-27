n = 4
lst = list()
for i in range(n):
    lst.append([0]*4)
for i in range(n):
    for j in range(n):
        if i == j:
            lst[i][j] = 1
        elif i > j:
            lst[i][j] = 2
        else:
            lst[i][j] = 0    

for n in lst:
    print(n)
