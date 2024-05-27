from datetime import datetime, timedelta

def registration():
    reg = input("Вы хотите начать процедуру регистрации? (да, нет): ")
    fio1 = []
    dt1 = []
    balance1 = []
    while reg != "нет":
        fio = input("Введите Фамилию Имя и Отчество пользователя: ")
        fio1.append(fio)
        past_date = datetime.today() - timedelta(days=6575)
        print("Дата рождения нового пользователя не должна быть больше, чем: ", past_date)
        try:
            dt = int(input("Введите дату рождения в формате ГГГГММДД: "))
            dt1.append(dt)
        except ValueError:
            print("Ошибка: введенная дата не соответствует формату ГГГГММДД.")
        balance = int(input("Введите баланс кошелька: "))
        balance1.append(balance)
        reg = input("Вы хотите начать процедуру регистрации? (да, нет): ")
        users = {
            "Имена пользователей": fio1,
            "Даты рождения пользователя": dt1,
            "Баланс кошелька": balance1
        }
        print(users)

def authorization():
    autorization_name = input("Введите имя пользователя: ")
    autorization_pass = input("Введите пароль: ")
    if autorization_name != "admin" or autorization_pass != "551122":
        print("Доступ запрещен!")
    else:
        registration()

authorization()