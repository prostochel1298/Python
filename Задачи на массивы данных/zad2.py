class Soda():
    def __init__(self,feeling=None):
        self.feeling = feeling
    def show_my_drink(self):
        if self.feeling != None:
            print("Газировка и",self.feeling)
        else:
            print("Обычная газировка")

pepsi = Soda()
pepsi.show_my_drink()

    