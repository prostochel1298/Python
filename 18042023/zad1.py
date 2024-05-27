class Card:
    def __init__(self,card_name,balance):
        self.card_name = card_name
        self.__balacne = balance
    def name(self):
        print("Ваша платежная систем:", self.card_name,"Ваш баланс:",self.__balacne)
    def __passw(self):
        a = input("Для активации бонуса введите промокод: ")
        if a == "babayaga":
            return 500
        elif a == "koshey":
            return 1000
        elif a == "kolobok":
            return 2000
        else:
            return -1
    def activation(self):
        b = self.__passw()
        if b >= 0:
            self.__balacne=b
            print("Ваш баланс на карте:",self.__balacne)
        else:
            print("Вы ввели неправильный пар")

            

bank = Card("ДНС",0)
bank.name()
bank.activation()


