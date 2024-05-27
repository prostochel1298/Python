from time import sleep
class Serf:
    def __init__(self,name,health,power,money,armor,weapon):
        self.name = name
        self.health = health
        self.power = power
        self.money = money
        self.armor = armor
        self.weapon = weapon
    def info(self):
        print("Ваше имя:",self.name,"Уровень здоровья:",self.health,"Ваша сила:",self.power,"Ваши деньги:",self.money,"Уровень брони:",self.armor,"Ваше оружие",self.weapon)
    def attack(self,enemy):
        while self.armor and enemy.armor > 0:
            self.armor-=enemy.power
            enemy.armor-=self.power
        if self.armor and enemy.armor<=0:
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

ivan = Serf("Иван",100,30,0,0,"Рука")
print("Предствим вашего игрока:")

sleep(1)
ivan.info()
sleep(1)

class Petushara(Serf):
    def inf(self):
        print("Имя врага:",self.name,"Уровень здоровья:",self.health,"Сила",self.power,"Деньги:",self.money,"Уровень брони:",self.armor,"Оружие",self.weapon)
robber = Petushara("Кузьма",100,15,25,0,"Рука")

class Torgash(Serf):
    def inf1(self):
        print("Имя персонажа:",self.name)
        

merchant = Torgash("Торгаш",0,0,0,0,"Рука")

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
ivan.info()
def buy():
    buy1 = input("Вы в торговой лавке, что предпочтете купить?(У нас есть броня за - 15 монет, вы можете восстановить здоровье - 10 монет или купить оружие(цена зависит от вида)),для выхода напишите слово'выход': ")
    while buy1 != "выход":
        if buy1 == "броня":
            if ivan.money >= 15:
                ivan.money -=15
                ivan.armor = 100
                print("Вы купли броню, теперь уровень вашей защиты:",ivan.armor,"Остаток денег:",ivan.money)

            elif ivan.money<15:
                print("У вас недостаточно монет!")
        elif buy1 == "здоровье":
            if ivan.money >=10:
                ivan.money -=10
                ivan.health = 100
                print("Вы восстановили здоровье, теперь его уровень:",ivan.health,"Остаток денег:",ivan.money)
            else:
                print("У вас недостаточно монет!")
            
        buy1 = input("Вы в торговой лавке, что предпочтете купить?(У нас есть броня за - 15 монет, вы можете восстановить здоровье - 10 монет или купить оружие(цена зависит от вида)),для выхода напишите слово'выход': ")                

buy()
ivan.info()
gnida = Petushara("Залупа",120,15,25,30,"Рука")
ivan.attack(gnida)