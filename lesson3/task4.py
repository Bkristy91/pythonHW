# Задание №4
# Программа принимает действительное положительное число x и целое отрицательное число
# y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
# в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
# помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def my_func1(x, y):
    return x ** y

def my_func2(x, y):
    res = 1
    for i in range(abs(y)):
        res = res * x
    return 1 / res

numb1 = int(input('Введите первый аргумент: '))
numb2 = int(input('Введите второй аргумент: '))

print(f'Результат: {my_func1(numb1, numb2)}') #возведение числ в степень через **

print(f'Результат: {my_func2(numb1, numb2)}') #возведение числ в степень через цикл