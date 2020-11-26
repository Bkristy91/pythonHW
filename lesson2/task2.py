# Задание №2
# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

countList = int(input('Введите количество элементов списка: '))
myList = []

for i in range(countList):
    myList.append(input(f'Введите {i + 1}ый элемент списка: '))

print(f'Пользовательский список: {myList}')

numberIterations = int(len(myList)/2)

for i in range(numberIterations):
    temp = myList[2 * i]
    myList[2 * i] = myList[2 * i + 1]
    myList[2 * i + 1] = temp

print(f'Измененный список: {myList}')
