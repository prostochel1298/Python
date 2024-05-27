from random import randint
from time import sleep

class NPC():
    def __init__(self,name,health):
        self.name = name
        self.health = health


class Swordsman(NPC):
    def __init__(self, name, health,power):
        super().__init__(name, health)
        self.power = power
    def attakeishn(self,enemy):
        while self.health > 0:
            print("Мечник атакует")
            enemy.health = enemy.health - self.power
            self.health = self.health - enemy.mana*2
            if self.health<=0:
                print("Game over")
            print("У вас осталось здоровья: ", self.health)
            print("У противника осталось здоровья: ",enemy.health)
            sleep(2)


class Mag(NPC):
    def __init__(self, name, health,mana,power):
        super().__init__(name, health)
        self.mana = mana
        self.power = power
    def mag_ebanariy(self,enemy):
        while self.mana > 0:
            print("Маг-ебанарий применяет свой магический челнок")
            sleep(2)
            self.mana = self.mana - 1
            enemy.health = enemy.health - self.mana*2
            self.health = self.health - enemy.power
            if self.mana<=0:
                print("У вас закончилась мана")
            elif self.health<=0:
                print("Game over")
            print("У вас осталось здоровья: ", self.health)
            print("У противника осталось здоровья: ",enemy.health)
            print("У вас осталось маны: ",self.mana)
            sleep(2)

m1 = Swordsman("Клитор первый", 13,randint(0,5))       
m2 = Mag("Ебанарий",10,3,0)
m1.attakeishn(m2) 