import math
zapros = input("Площадь какой из предложенных фигур вы хотите посчитать?(Квадрат,Треугольник, Круг,Прямоугольник)?: ").lower()
if zapros == "квадрат":
    lenn = input("Введите длину стороны: ")
    while True:
        try:
            lenn = int(lenn)
            print("Площадь квадрата равна:",lenn**2)
            break
        except:
            lenn = input("Введи число, тупая, ты пизда: ")
elif zapros == "треугольник":
    h = input("Введите высоту:")
    while True:
        try:
            h = int(h)
            break
        except:
            h = input("Открой математику за первый класс, раздел 'Числа'^:")
    o = input("Введите основание:")        
    while True:
        try:
            o = int(o)
            print("Площадь треуголька равна:",o/2*h)
            break
        except:
            o = input("Ну и нахрена ты опять ввела слово 'основание'?? Нормально введи:")
elif zapros == "круг":
    r = input("Введите радиус как число:")
    while True:
        try:
            r = int(r)
            print("Площадь круга равна:",math.pi*r**2)
            break
        except:
            input("ты внатуре недалекая, ЧИСЛО ВВЕДИ, ОДНО, БЛЯТЬ, ЧИСЛО")
elif zapros == "прямоугольник":
    a = input("Введите одну сторону:")
    while True:
        try:
            a = int(a)
            break
        except:
            a = input("Открой математику за первый класс, раздел 'Числа'^:")
    b = input("Введите другую сторону:")        
    while True:
        try:
            b = int(b)
            print("Площадь треуголька равна:",a*b)
            break
        except:
            o = input("Ну и нахрена ты опять ввела слово 'основание'?? Нормально введи:")

    
            