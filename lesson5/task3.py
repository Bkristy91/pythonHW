# Задание №3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
# -*- codecs: utf-8 -*-
import codecs

listSalary = list()
with codecs.open('employees.txt', 'r', 'utf-8') as f_obj:
    for line in f_obj:
        dataNameSalary = line.split()
        if float(dataNameSalary[1]) < 20000:
            print(dataNameSalary[0])
        listSalary.append(float(dataNameSalary[1]))

print(f'Средний доход сотрудников {sum(listSalary) / len(listSalary)}')
