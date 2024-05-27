class Person:
    def __init__(self,first_name,last_name,age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
    
    def __check_passw(self):
        a = int(input("Введите пароль: "))
        if a == 234566:
            return True
        else:
            print("Неправильный пароль")
    def set_age(self):
        b = self.__check_passw()
        if b == True:
            self.__age = int(input("Введите желаемый возраст"))
            print("Ваш возраст:", self.__age)

Darya = Person("Дарья","Одинцова",23)
Darya.set_age()

                                   
