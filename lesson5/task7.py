# Задание №7
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать .
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
# Подсказка: использовать менеджер контекста.
# -*- codecs: utf-8 -*-
import codecs
import json

dictFirm = dict()
average_profit = 0
n = 0
with codecs.open('firm.txt', 'r', 'utf-8') as f_obj:
    for line in f_obj:
        listFirm = line.split()
        profit = int(listFirm[2]) - int(listFirm[3])
        dictFirm[listFirm[0]] = profit
        if profit > 0:
            n += 1
            average_profit += profit

dictAverageProfit = {'average_profit': average_profit / n}
listFirm = [dictFirm, dictAverageProfit]
print(listFirm)

with open( "firm.json" , "w") as write_f:
    json.dump(listFirm, write_f)



