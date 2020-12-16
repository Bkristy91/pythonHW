# Задание №5
# Реализовать класс Stationery ( канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw ( отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen ( ручка), Pencil ( карандаш), Handle ( маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    title = 'Stationery'

    def drow(self):
        print('Запуск отрисовки')

class Pencil(Stationery):

    def drow(self):
        print('Рисование карандашом')

class Handle(Stationery):

    def drow(self):
        print('Рисование маркером')

class Pen(Stationery):

    def drow(self):
        print('Рисование ручкой')


objStationery = Stationery()
objPen = Pen()
objPencil = Pencil()
objHandle = Handle()

listStationery = [objStationery, objPen, objPencil, objHandle]
for el in listStationery:
    el.drow()