# Задание №1
# Создать класс TrafficLight ( светофор) и определить у него один атрибут color ( цвет) и метод
# running ( запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def color_red(self):
        self.__color = 'red'
        print(self.__color)
        time.sleep(7)

    def color_yellow(self):
        self.__color = 'yellow'
        print(self.__color)
        time.sleep(2)

    def color_green(self):
        self.__color = 'green'
        print(self.__color)
        time.sleep(5)

    def running(self):
        if self.__color == 'red':
            self.color_red()
            self.color_yellow()
            self.color_green()
        elif self.__color == 'yellow':
            self.color_yellow()
            self.color_green()
            self.color_red()
        elif self.__color == 'green':
            self.color_green()
            self.color_red()
            self.color_yellow()

        print('Stop')


b = TrafficLight('green')
b.running()
