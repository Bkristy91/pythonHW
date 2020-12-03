# Задание №5
# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.
from functools import reduce
import random


def my_sum(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el


# создание файла со случаными числами
with open('my_file_numb.txt', 'w') as f_obj:
    for i in range(10):
        print(random.randint(0, 10), end=' ', file=f_obj)

listNumb = list()
with open('my_file_numb.txt', 'r') as f_obj:
    for line in f_obj:
        for el in line.split():
            listNumb.append(int(el))

print(reduce(my_sum, listNumb))
