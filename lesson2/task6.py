# Задание №6
# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Объявляем характеристики товара, которые будут использоваться в структуре данных "Товар"
listProduct = []
name = 'название'
cost = 'цена'
count = 'количество'
unit = 'eд'
# Объявляем списки, которые будет использовать в аналитике
listName = list()
listCost = list()
listCount = list()
listUnit = list()

# Запрашиваем количество товаров в структуре "Товары"
numbProducts = int(input('Введите количество товаров: '))

for i in range(numbProducts):
    # Собираем данные о товаре
    nameProduct = input('Введине наименование товара: ')
    costProduct = input('Введине цену товара: ')
    countProduct = input('Введине количество товара: ')
    unitProduct = input('Введине единицу измерения товара: ')
    dictProduct = {name: nameProduct, cost: costProduct, count: countProduct, unit: unitProduct}
    listName.append(dictProduct.get(name))
    listCost.append(dictProduct.get(cost))
    listCount.append(dictProduct.get(count))
    listUnit.append(dictProduct.get(unit))
    # Формируем кортеж
    cortegeProduct = (i + 1, dictProduct)
    # Добавляем в структуру
    listProduct.append(cortegeProduct)

print()
print('Структура "Товары"')
for el in listProduct:
    print(el)

dictAnalysis = {name: listName, cost: listCost, count: listCount, unit: listUnit}
print()
print('Аналитика товаров')
for key, value in dictAnalysis.items():
    print(f'{key}: {value}')
