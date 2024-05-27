scrable = {"авенорст":1,"дклмпу":2,
           "йы":3,"жзхцч":5,"шэю":8,"фщъ":10}
word = input("Введите слово: ")
score = 0
b = scrable.keys()
for i in b:
    for a in i:
        if a in word:
            score+=scrable[i]
print(score)

         
