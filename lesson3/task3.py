# Задание №3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(avg1, avg2, avg3):
    return avg1 + avg2 + avg3 - min(min(avg1, avg2), avg3)

numb1 = int(input('Введите первый аргумент: '))
numb2 = int(input('Введите второй аргумент: '))
numb3 = int(input('Введите третий аргумент: '))

print(f'Сумма: {my_func(numb1, numb2, numb3)}')