# Задание№1
name = 'Default'
year = 5
city = ''

name = input('Введите ваше имя: ')
year = int(input('Введите год вашего рождения: '))
city = input('Введите из какого вы города: ')
experience = int(input('Введите сколько лет вы занимаетесь программированием: '))

print(f'Резюме {name}.')
print(f'Возраст соискателя: {str(2020-year)} лет. Город проживания: {city}.')
print(f'Стаж программирования: {experience}')