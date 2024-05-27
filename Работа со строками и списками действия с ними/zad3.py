score = input("Введите пять оценок через пробел: ")
sc=score.split(" ")
sc1 = []
for i in sc:
    i=int(i)
    sc1.append(i)
print("Необходимо повторение материала:",(sum(sc1)/len(sc1))<=3.5)
