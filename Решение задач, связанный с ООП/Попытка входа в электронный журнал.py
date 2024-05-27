class Student:
    def __init__(self,student_name,score):
        self.student_name = student_name
        self.__score = score
    def info(self):
        print(self.student_name,self.__score)
    def __one_step(self):
        print("Для того, чтобы изменить данные необходимо ввести логин и пароль от лчиного кабинета учителя!")
        login = "director"
        passw = "773344"
        b = input("Введите логин: ")
        c = input("Введите пароль: ")

        if b == login and c == passw:
            return True
        else:
            print("Вы ввели неправильный пароль, скорее, что вы ученик, за попытку взлома будут вызваны ваши родители!")
    def two_step(self):
        g = self.__one_step()
        if g == True:
            d = input("Доступ разрешен! Введите новую оценку: ")
            self.__score = d
vasya = Student("Вася",2)
vasya.two_step()
vasya.info()   


