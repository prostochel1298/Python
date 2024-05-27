a4 = {'pos':lambda x: x-1, 'neg':lambda x: abs(x)-1, 'zero':lambda x: x}
b = [-3, 10, 0, 1]
for i in b:
    if i < 0:
        print(a4['neg'](i))
    elif i > 0:
        print(a4['pos'](i))
    else:
        print(a4['zero'](i))