def calculate():
    operation = input('Выберите операцию (+, -, *, /): ')
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print('Ошибка! Деление на ноль.')
        else:
            print(num1 / num2)
    else:
        print('Ошибка! Выбрана неверная операция.')

calculate()