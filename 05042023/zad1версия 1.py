from time import sleep
class Serf:
    def __init__(self,name,health,power,money=0):
        self.name = name
        self.health = health
        self.power = power
        self.money = money
    def info(self):
        print("Ваше имя:",self.name,"Уровень здоровья:",self.health,"Ваша сила:",self.power,"Ваши деньги:",self.money)
    def attack(self,enemy):
        while self.health and enemy.health > 0:
            self.health-=enemy.power
            enemy.health-=self.power
        if self.health <= 0:
            print("Вы погибли")
        elif enemy.health <= 0:
            print("Ваш враг повержен")
            self.money+=enemy.money
    

print("Добро пожаловть в квест 'Путь раба'")
sleep(1)
print("Вам предстоит путешествие по древней Руси от простого крепостного до князя со своим царством")
sleep(1)
print("На вашем пути будет множество испытаний, пройти которые сможет лишь избранный молодец")

ivan = Serf("Иван",100,30)
print("Предствим вашего игрока:")
sleep(1)
ivan.info()
sleep(1)

class Petushara(Serf):
    def inf(self):
        print("Имя врага:",self.name,"Уровень здоровья:",self.health,"Сила",self.power,"Деньги:",self.money)

class Torgash(Serf):
    def inf1(self):
        print("Имя персонажа:",self.name)
    
        
        
class SerfinArmor(Serf):
    def __init__(self,name, health, power, money,armor):
        self.armor = armor
        super().__init__(name,health,power,money)     
    def infarmor(self):
        print("Ваше имя:",self.name,"Уровень здоровья:",self.health,"Ваша сила:",self.power,"Ваши деньги:",self.money,"Уровень брони:",self.armor)
        
robber = Petushara("Кузьма",100,15,25)
merchant = Torgash("Торгаш")
print("В день летнего солнцестояния вы собирали урожай...")
sleep(1)
print("Внезапно на вашей земле появляется Кузьма и просит отдать силой весь свой урожай")
sleep(1)
print("Вы готовы драться...")
ivan.info()
sleep(1)
robber.inf()
sleep(1)
print("Начинается битва")
sleep(1)
ivan.attack(robber)

