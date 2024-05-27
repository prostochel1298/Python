grades = {"Иванов":5, "Смирнов":3, "Пупкин":4, "Соловьева":3, "Сомова":5}
b=list(grades.items())
c=[]
for i in b:
    if i[1]>3:
        c.append(i[0])
print(c)

    