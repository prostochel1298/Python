ankety = {"Васильев":{
    "Увлечения":"Рыбалка",
    "Возраст":"23 года"
    },
        "Иванов":{
            "Увлечения":"Программирование",
            "Возраст":"21 год"
        },
        "Малиновский":{
            "Увлечения":"Фотография",
            "Возраст":"26 лет"
        }       
}

while True:
    create_anketa = input("Для того чтобы создать анкету для начала напишите свою фамилию(стоп - остановить, а для того чтобы удалить анкету - удалить ): ")
    if create_anketa == "удалить":
        del_name = input("Какую фамилию хотите удалить?: ")
        del ankety[del_name]
    elif create_anketa == "стоп":
        break
    dop_question = input("Добавить увлечения и возраст?: ")
    if dop_question == "да":
        create_hobby = input("Напишите ваше увлечение: ")
        create_age = input("Введите ваш возраст: ")
        hb_age = dict()
        hb_age["Увлечения"] = create_hobby
        hb_age["Возраст"] = create_age
        ankety[create_anketa] = hb_age
    else:
        break
    




print("Все анкеты:", ankety)


name = input("Введите фамилию: ")
for i in ankety[name]:
    print(i,"-",ankety[name][i])