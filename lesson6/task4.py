# Задание №4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, i s_police ( булево). А также методы: go, stop, t urn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# ( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    class_name = 'Car'

    def __init__(self, name, class_name='Car'):
        self.name = name
        self.speed = 0
        self.color = 'white'
        self.is_police = False
        self.class_name = class_name
        print(f'{self.class_name} with name {self.name} completed')

    def show_attributes(self):
        print(f'name: {self.name}, speed: {self.speed}, color: {self.color}, s_police: {self.is_police}')

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} drove with {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'{self.name} stop')

    def turn(self, direction):
        print(f'{self.name} turn on {direction}')

    def show_speed(self):
        print(f'{self.name} speed {self.speed}')

# дочерние TownCar, SportCar, WorkCar, PoliceCar
class TownCar(Car):

    def __init__(self, name):
        self.class_name = 'TownCar'
        super().__init__(name, self.class_name)
        self.color = 'gray'

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} exceeded the speed for this class of cars, 60км/h')
        else:
            print(f'{self.name} speed {self.speed}')

class SportCar(Car):
    def __init__(self, name):
        self.class_name = 'SportCar'
        super().__init__(name, self.class_name)
        self.color = 'red'

class WorkCar(Car):
    def __init__(self, name):
        self.class_name = 'WorkCar'
        super().__init__(name, self.class_name)
        self.color = 'yellow'

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} exceeded the speed for this class of cars, 40km/h')
        else:
            print(f'{self.name} speed {self.speed}')

class PoliceCar(Car):
    def __init__(self, name):
        self.class_name = 'PoliceCar'
        super().__init__(name, self.class_name)
        self.is_police = True
        self.color = 'blue'


carKira = Car('Kira')
carMax = TownCar('Max')
carTim = SportCar('Tim')
carAlice = WorkCar('Alice')
carJone = PoliceCar('Jone')
print('')

listStationery = [carKira, carMax, carTim, carAlice, carJone]
for el in listStationery:
    el.show_attributes()
    el.go(100)
    el.show_speed()
    el.turn('left')
    el.stop()
    print('')
