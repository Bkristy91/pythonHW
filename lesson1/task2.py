# Задание№2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('Введите время в секундах'))

hours = int(time /3600)
minutes = int((time - hours * 3600) / 60)
seconds = time % 60

#print('Часов: ' + str(hours) + ' минут: ' + str(minutes) + ' секунд: ' + str(seconds)) #проверка расчетов

if minutes < 10:
    minutesStr = '0' + str(minutes)
else:
    minutesStr = str(minutes)

if seconds < 10:
    secondsStr = '0' + str(0 + seconds)
else:
    secondsStr = str(seconds)

print(f'{hours}:{minutesStr}:{secondsStr}')