# Задание №4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.
# -*- codecs: utf-8 -*-
import codecs

dictRus = {
    1: 'Первый',
    2: 'Второй',
    3: 'Третий',
    4: 'Четвертый'
}
newList = list()
with open('numerals.txt', 'r') as f_obj:
    for line in f_obj:
        wordsList = line.split()
        newList.append(f'{dictRus[int(wordsList[2])]} - {wordsList[2]}')

with codecs.open('numeralsRus.txt', 'w', 'utf-8') as f_obj:
    for line in newList:
        print(line, file=f_obj)

print(newList)
