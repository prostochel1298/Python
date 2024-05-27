# -*- coding: utf-8 -*-

logg = input("Добро пожаловать в backofice театра 'амстердам'. Введите логин для входа в систему:  ")
pas = input("Введите пароль: ")


def afisha():
    print("Список театральных постановок: ")
    print("Недоросоль\nПапа\nДубровский\nТы где-то рядом\nИмператор")
    teatr = input("Введите постановку, которая вас интересует: ").lower()
    if teatr == "недоросоль":
        print("1-место занято,0-место свободно")
        spisok_mest = [[0,0,1,0,1,1,1,0],[1,1,1,1,0,0,1,0],[0,1,1,0,0,1,0,1],[0,0,0,0,0,1,1,0],[1,0,0,1,1,0,1,0],[0,0,0,1,0,1,0,0],[1,1,0,0,0,1,1,0],[0,0,1,1,1,1,0,1]]
        for i in spisok_mest:
            print(i)
        mesta = input("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
        while mesta == "1" or mesta == "2":
            if mesta == "1":
            
                ryad = int(input("Выберете ряд(от 1 до 8):"))
                mesto = int(input("Выберете место: "))
                if spisok_mest[ryad - 1][mesto - 1] == 1:
                    print("Место занято, выберете другое место")
                    mesta = input("забронировать место?да/нет: ").lower()
                    for i in spisok_mest:
                        print(i)
                else:
                    spisok_mest[ryad - 1][mesto - 1] = 1
                for i in spisok_mest:
                    print(i)
                mesta = input("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
            elif mesta == "2":
                ryad = int(input("Выберете ряд(от 1 до 8):"))
                mesto = int(input("Выберете место: "))
                spisok_mest[ryad - 1][mesto - 1] = 0
                for i in spisok_mest:
                        print(i)
                mesta = input ("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()

        
                    

            
            


    elif teatr == "папа":
        print("1-место занято,0-место свободно")
        spisok_mest = [[0,1,1,0,0,0,1,0],[0,1,0,1,0,1,1,0],[1,0,1,0,1,1,0,1],[1,0,1,0,0,0,1,0],[1,1,1,1,1,0,1,0],[1,0,1,1,0,1,1,0],[1,1,0,1,0,1,0,1],[1,1,1,1,1,1,0,1]]
        for i in spisok_mest:
            print(i)
        mesta = input("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
        while mesta == "1" or mesta == "2":
            if mesta == "1":
            
                ryad = int(input("Выберете ряд(от 1 до 8):"))
                mesto = int(input("Выберете место: "))
                if spisok_mest[ryad - 1][mesto - 1] == 1:
                    print("Место занято, выберете другое место")
                    mesta = input("забронировать место?да/нет: ").lower()
                    for i in spisok_mest:
                        print(i)
                else:
                    spisok_mest[ryad - 1][mesto - 1] = 1
                for i in spisok_mest:
                    print(i)
                mesta = input("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
            elif mesta == "2":
                ryad = int(input("Выберете ряд(от 1 до 8):"))
                mesto = int(input("Выберете место: "))
                spisok_mest[ryad - 1][mesto - 1] = 0
                for i in spisok_mest:
                        print(i)
                mesta = input ("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
    elif teatr == "дубровский":
        print("1-место занято,0-место свободно")
        spisok_mest = [[1,1,0,0,1,0,1,0],[0,1,1,1,0,1,1,1],[0,0,1,1,0,1,0,1],[1,1,1,1,0,0,0,0],[1,1,0,1,1,0,1,0],[1,0,0,1,1,0,1,0],[0,0,1,1,0,1,0,0],[1,1,0,1,0,1,0,1]]
        for i in spisok_mest:
            print(i)
        mesta = input("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
        while mesta == "1" or mesta == "2":
            if mesta == "1":
            
                ryad = int(input("Выберете ряд(от 1 до 8):"))
                mesto = int(input("Выберете место: "))
                if spisok_mest[ryad - 1][mesto - 1] == 1:
                    print("Место занято, выберете другое место")
                    mesta = input("забронировать место?да/нет: ").lower()
                    for i in spisok_mest:
                        print(i)
                else:
                    spisok_mest[ryad - 1][mesto - 1] = 1
                for i in spisok_mest:
                    print(i)
                mesta = input("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
            elif mesta == "2":
                ryad = int(input("Выберете ряд(от 1 до 8):"))
                mesto = int(input("Выберете место: "))
                spisok_mest[ryad - 1][mesto - 1] = 0
                for i in spisok_mest:
                        print(i)
                mesta = input ("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
    elif teatr == "ты где-то рядом":
        print("1-место занято,0-место свободно")
        spisok_mest = [[1,1,1,0,1,0,1,0],[0,1,0,1,1,1,1,1],[0,0,0,1,0,0,0,1],[1,1,0,1,0,1,0,0],[1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,0],[1,1,1,1,0,1,0,0],[1,0,0,1,0,0,0,1]]
        for i in spisok_mest:
            print(i)
        mesta = input("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
        while mesta == "1" or mesta == "2":
            if mesta == "1":
            
                ryad = int(input("Выберете ряд(от 1 до 8):"))
                mesto = int(input("Выберете место: "))
                if spisok_mest[ryad - 1][mesto - 1] == 1:
                    print("Место занято, выберете другое место")
                    mesta = input("забронировать место?да/нет: ").lower()
                    for i in spisok_mest:
                        print(i)
                else:
                    spisok_mest[ryad - 1][mesto - 1] = 1
                for i in spisok_mest:
                    print(i)
                mesta = input("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
            elif mesta == "2":
                ryad = int(input("Выберете ряд(от 1 до 8):"))
                mesto = int(input("Выберете место: "))
                spisok_mest[ryad - 1][mesto - 1] = 0
                for i in spisok_mest:
                        print(i)
                mesta = input ("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
    elif teatr == "император":
        print("1-место занято,0-место свободно")
        spisok_mest = [[1,0,0,0,1,1,1,0],[0,1,1,1,0,1,1,1],[0,1,1,1,0,0,0,1],[1,0,0,1,0,1,0,1],[0,1,0,0,0,0,1,0],[1,1,1,0,1,0,1,0],[1,1,0,1,0,1,0,0],[1,1,0,1,1,1,0,1]]
        for i in spisok_mest:
            print(i)
        mesta = input("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
        while mesta == "1" or mesta == "2":
            if mesta == "1":
            
                ryad = int(input("Выберете ряд(от 1 до 8):"))
                mesto = int(input("Выберете место: "))
                if spisok_mest[ryad - 1][mesto - 1] == 1:
                    print("Место занято, выберете другое место")
                    mesta = input("забронировать место?да/нет: ").lower()
                    for i in spisok_mest:
                        print(i)
                else:
                    spisok_mest[ryad - 1][mesto - 1] = 1
                for i in spisok_mest:
                    print(i)
                mesta = input("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
            elif mesta == "2":
                ryad = int(input("Выберете ряд(от 1 до 8):"))
                mesto = int(input("Выберете место: "))
                spisok_mest[ryad - 1][mesto - 1] = 0
                for i in spisok_mest:
                        print(i)
                mesta = input ("забронировать место?(1-забронировать,2-отменить бронь, 0 - выйти): ").lower()
n = 1
while n < 3:
    if logg == "admin" and pas == "dddd":
        afisha()
        break
    else:
        print("Вы ввели не верный пароль или логин, повторите попытку")
        n+=1
        logg = input("Добро пожаловать в backofice театра 'амстердам'. Введите логин для входа в систему:  ")
        pas = input("Введите пароль: ")
        



