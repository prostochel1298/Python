chisla = [5,9]
b = [0]
n = 5
while n!=9:
    b.append(chisla[0])
    for i in b:
        if i >=5:
            b.append(i)
            i+=1
print(b)
