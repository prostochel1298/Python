class Women:
    def __init__(self):
        self.age = 34
    def doctor(self):
        print("Вам необходимо посетить следующих врачей для мед.осмотра:'Невролог,Хирург,Эндокринолог,Гинеколог,Гематолог,Нарколог'")

class Men:
    def __init__(self):
        self.age = 34
    def doctor(self):
        print("Вам необходимо посетить следующих врачей для мед.осмотра:'Офтальмолог,Хирург,Эндокринолог,Уролог,Психиатр,Кардиолог'")

Natasha = Women()
Natasha.doctor()
Oleg = Men()
Oleg.doctor()
Masha = Women()
Masha.doctor()