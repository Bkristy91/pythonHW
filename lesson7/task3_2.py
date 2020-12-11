# Задача №3
# Про клетки
class Cage:
    def __init__(self, count_cage):
        self.count_cage = count_cage

    def __add__(self, other):
        return Cage(self.count_cage + other.count_cage)

    def __sub__(self, other):
        return Cage(self.count_cage - other.count_cage if self.count_cage > other.count_cage else print('Недостаточно клеток'))

    def __mul__(self, other):
        return Cage(self.count_cage * other.count_cage)

    def __truediv__(self, other):
        return Cage(self.count_cage // other.count_cage)

    def make_order(self, count_cage_line=10):
        ost = self.count_cage % count_cage_line
        for i in range(0, self.count_cage // count_cage_line):
            print('*' * count_cage_line)
        if ost > 0:
            print('*' * ost)


a = Cage(10)
b = Cage(6)
c = a + b
print(f'Сложение: {c.count_cage}')
c.make_order(5)
d = a - b
print(f'Вычитание: {d.count_cage}')
d.make_order()
f = a / b
print(f'Деление: {f.count_cage}')
f.make_order()
m = a * b
print(f'Умножение: {m.count_cage}')
m.make_order()

