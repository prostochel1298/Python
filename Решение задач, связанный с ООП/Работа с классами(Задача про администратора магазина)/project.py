class Admin:
    def __init__(self,mag_name,tovar,price):
        self.mag_name = mag_name
        self.price = price
        self.tovar = tovar
    def info(self):
        print("Наименование магазина",self.mag_name,"Ваш товар: ", self.tovar,"Цена: ",self.price)
    def stat(self):
        print("Ваша статистика администратора: часов онлайн: 150, забанено пользователей: 10")
    def __password(self):
        print("Чтобы зайти под именем администратора введите логин и пароль")
        login = "admin"
        passs = "12344321"
        a = input("Ввелите логин: ")
        b = input("Введите пароль: ")

        if a == login and b == passs:
            return True
        else:
            print("Вы ввели неправильный логин и пароль!")
    
    def new_price(self):
        c = self.__password()
        if c == True:
            d = self.price - (self.price*0.1)
            print("Вы ввели верный пароль, цена со скидкой: ",d)
class User:
    def __init__(self,mag_name,tovar,price):
        self.mag_name = mag_name
        self.price = price
        self.tover = tovar
    def stat(self):
        print("Ваша статистика пользователя: часов онлайн: 150, куплено товаров: 14, сумма купленных товаров: 25300 рублей")

class Admin2:
    def __init__(self,mag_name,tovar,price,admin_spisok):
        super().__init__(mag_name,tovar,price,admin_spisok)
    def sps(self):
        print("Список всех админов сайта: vasya123, nagibator2010,zhoporez231")




sumka= Admin("Пятерочка","Сумка",500)

lol = User("Петерочка","Пальто",400)

admin2 = Admin
