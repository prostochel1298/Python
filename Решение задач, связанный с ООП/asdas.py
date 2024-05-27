class Goom(object):
    items = []

    def __init__(self, name, seats, jump):
        """Инициализация"""
        self.name = name
        self.seats = seats
        self.jump = jump
        Goom.items.append(self)

    def __str__(self):
        return "{} {} {}".format(self.name, self.seats, self.jump)


my_goom1 = Goom("Лил", "1", "Нет")
my_goom2 = Goom("Мак", "1", "Есть")
my_goom3 = Goom("Ной", "1", "Есть")

print(Goom.items[0])