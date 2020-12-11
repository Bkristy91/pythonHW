# Задание №3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через список
try:
    numbMonth = int(input('Введите номер месяца в виде целого числа от 1 до 12: '))
except ValueError:
    numbMonth = 0

monthListWinter = [12, 1, 2]
monthListSpring = [3, 4, 5]
monthListSummer = [6, 7, 8]
monthListAutumn = [9, 10, 11]

if (numbMonth >= 1) and (numbMonth <= 12):
    if numbMonth in monthListWinter:
        month = 'зима'
    elif numbMonth in monthListSpring:
        month = 'весна'
    elif numbMonth in monthListSummer:
        month = 'лето'
    elif numbMonth in monthListAutumn:
        month = 'осень'
    print(f'Время года: {month}')
else:
    print('Необходимо ввести целое число от 1 до 12')

# Решение через словарь
dictMonth = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
if (numbMonth >= 1) and (numbMonth <= 12):
    print(f'Время года: {dictMonth.get(numbMonth)}')
else:
    print('Необходимо ввести целое число от 1 до 12')
