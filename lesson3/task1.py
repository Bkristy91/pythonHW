# Задание №1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devision (arg1, arg2):
    try:
        result = arg1 / arg2
    except ZeroDivisionError:
        return 'Ошибка. Деление на 0'

    return 'Результат: ' + str(round(arg1 / arg2,2))

number1 = int(input('Введите число 1: '))
number2 = int(input('Введите число 2: '))

print(devision(number1, number2))