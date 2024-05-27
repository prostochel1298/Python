from datetime import*
from random import randint 
def registration():
    reg = input("Вы хотите начать процедуру регистрации?(да,нет): ")
    fio1=dict()
    dt1=dict()
    balance1=dict()
    users = dict()
    while reg != "нет":
        fio = input("Введите Фамилию Имя и Отчетво пользователя: ")
        fio1["ID"]=fio
        past_date = datetime.today() - timedelta(days=6575)
        print("Дата рождения нового пользователя не должна быть больше, чем: ",past_date)
        dt = int(input("Введите дату рождения: "))
        dt1["Date_Birthday"] = dt
        balance = int(input("Ввести баланс кошелька: "))
        balance1["Balance"] = balance
        reg = input("Вы хотите начать процедуру регистрации?(да,нет): ")
        users["данные пользователей"] = (fio,dt1,balance1)
    print(users)
        #def stavka():
            #name_user = {}
            #b = 0
            #for i in users.values():
                    #name_user[i[0]] = balance1[b]
                    #i+=[1]
                    #b+=1
                    #break
            #print(name_user)
                
    #test_zapros = input("Хотите ли вы поставить ставку?(да или нет): ")
    #if test_zapros == "да":
        #stavka() 


#def autorization():
    #autorization_name = input("Введите имя пользователя: ")
    #autorization_pass = input("Введите пароль: ")
    #if autorization_name != "admin" and autorization_pass != 551122:
        #print("доступ запрещен!")
    #else:
        #registration()

registration()


