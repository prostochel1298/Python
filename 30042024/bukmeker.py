from datetime import*
from random import randint
def registration():
    reg = input("Вы хотите начать процедуру регистрации?(да,нет): ")
    fio1=list()
    dt1=list()
    balance1=list()
    while reg != "нет":
        fio = input("Введите Фамилию Имя и Отчетво пользователя: ")
        fio1.append(fio)
        past_date = datetime.today() - timedelta(days=6575)
        print("Дата рождения нового пользователя не должна быть больше, чем: ",past_date)
        dt = int(input("Введите дату рождения: "))
        dt1.append(dt)
        balance = int(input("Ввести баланс кошелька: "))
        balance1.append(balance)
        reg = input("Вы хотите начать процедуру регистрации?(да,нет): ")   
        users = {"Имена пользователей":fio1,
                  "Даты рождения пользователя":dt1,
                  "Баланс кошелька":balance1}
    print(users)
    def stavka():
        name_user = {}
        for i, k in zip(fio1,balance1):
            name_user[i]= k + 1
        id_vvod = input("Введите имя пользователя: ")
        if id_vvod in name_user.keys():
            bet = int(input("Сколько хотите поставить? "))
            bet+=1
            team = int(input("На кого хотите поставить?(1 - спартак,2 - зенит): "))
            if randint(0,1) == team:
                print("Вы победили")
                name_user[id_vvod]+=bet 
            else:
                print("ты проиграл!")
                name_user[id_vvod]-=bet 
            print("Ваше Имя:",id_vvod,"Ваш баланс:",name_user[id_vvod])
        else:
            print("Такого пользователя в базе нет!")
   
                
    test_zapros = input("Хотите ли вы поставить ставку?(да или нет): ")
    if test_zapros == "да":
        stavka() 


def autorization():
    autorization_name = input("Введите имя пользователя для авторизации: ")
    autorization_pass = input("Введите пароль: ")
    if autorization_name != "admin" and autorization_pass != 551122:
        print("доступ запрещен!")
    else:
        registration()
autorization()


