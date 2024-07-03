import re 
number = input("Введите автономер: ")
pattern_private = r"[австеконрухм]\w{3}[австеконрухм]{2}\w{2,3}" #владельцы обычных машин
pattern_taxi = r"[австеконрухм]{2}\w{3}\w{2,3}" #владельцы такси
while True:
    if re.fullmatch(pattern_private, number,flags=re.IGNORECASE):
        print("Частная машина")
    if re.fullmatch(pattern_taxi, number,flags=re.IGNORECASE):
        print("Это такси")
    number = input("Введите автономер: ")


