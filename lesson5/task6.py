# Задание №6
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
# -*- codecs: utf-8 -*-
import codecs


dictCountHour = dict()
with codecs.open('school_subject.txt', 'r', 'utf-8') as f_obj:
    for line in f_obj:
        sumHours = 0
        wordsList = line.split()
        for el in wordsList[1:]:
            numb_str = ''
            for letter in el:
                if '0' <= letter <= '9':
                    numb_str += letter
                else:
                    break
            if numb_str != '':
                sumHours += int(numb_str)
        school_subject = wordsList[0]
        dictCountHour[school_subject[:-1]] = sumHours

print(dictCountHour)

