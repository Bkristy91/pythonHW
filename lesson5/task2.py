# # Задание №2
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

dictLineWordInFile = dict()
n = 0
with open('my_file.txt', 'r') as f_obj:
    for line in f_obj:
        n += 1
        wordsList = line.split()
        dictLineWordInFile['строка ' + str(n)] = 'Количество слов: ' + str(len(wordsList))

print(dictLineWordInFile)