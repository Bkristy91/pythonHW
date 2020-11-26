# Задание №2
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. \
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def checkIn (name, surname, year, sity, email, phone):

    return (f'{name} {surname} {year} {sity} {email} {phone}')

name_user = input('Введите ваше имя: ')
surname_user = input('Введите вашу фамилию: ')
year_user = input('Введите год рождения: ')
sity_user = input('Введите город проживания: ')
email_user = input('Введите email: ')
phone_user = input('Введите телефон: ')

print(checkIn(name=name_user, surname=surname_user, year=year_user, sity=sity_user, email=email_user, phone=phone_user))