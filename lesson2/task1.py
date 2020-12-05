# Задание №1
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = list('list')
cortege = tuple('cortege')
many = set('many')
my_dict = dict(key='value')
temp = Warning
# вопрос: при проверке типа python указывает <class 'Warning'> - <class 'type' А почему так? Зарезервированное слово?

res_list = [125, 474.4, 'text', False, my_list, cortege, many, my_dict, b'text', None, temp]

for el in res_list:
    print(f'{el} - {type(el)}')

