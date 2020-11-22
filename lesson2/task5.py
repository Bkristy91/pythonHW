# Задание №5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating = [7, 5, 3, 3, 2]
listRating = list(rating)
newRank = int(input('Ведите новый элемент рейтинга: '))
lenListRating = len(listRating)

if newRank in listRating:
    countRepeat = listRating.count(newRank)
    listRating.insert(listRating.index(newRank) + countRepeat - 1, newRank)
# Вопрос. А нужно ли тут так заморачиваться, может достаточно вставить рейтинг после нахождения первого элемента?
# вот так: listRating.insert(listRating.index(newRank), newRank)
else:
    for i in range(lenListRating - 1):
        if (listRating[i] > newRank) and (listRating[i+1] < newRank):
            listRating.insert(i + 1, newRank)
            break
    else:
        if newRank > listRating[0]:
            listRating.insert(0, newRank)
        elif newRank < listRating[0]:
            listRating.append(newRank)

print(listRating)