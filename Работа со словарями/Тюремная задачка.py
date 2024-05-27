prison = {"Петров":1500,"Сидоров":1000,"Кочнев":500,"Гнидов":800,"Жопов":500}
market = {"Сигареты":200,"Чай":300,"Сахар":150,"Шампунь": 250,"Печенье":70,"Зубная паста":150,"Порошок":250,"Рулет":230}
print(prison.keys())
name = input("Выберете осужденного из списка: ")
print(prison[name])
name_tovar = input("Введите товар из списка: q - выйти ")
while name_tovar != "q":
    if prison[name] <=0:
        print("Баланс на нуле")
        break
    else:
        prison[name] = prison[name] - market[name_tovar]
        print(prison[name])
        name_tovar = input("Введите товар из списка: q - выйти ")
    
