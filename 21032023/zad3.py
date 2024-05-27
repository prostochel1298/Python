class Number():
    def __init__(self,string):
        self.string = string
    def get_String(self):
        self.string = input("Введите слово: ")
    def print_string(self):
        print(self.string.upper())
a = Number("xui")
a.get_String()
a.print_string()    