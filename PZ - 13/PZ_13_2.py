'''Если в двумерном списке имеются положительные элементы, то вывести TRUE,
иначе FALSE.'''

import random

while True:
    try:
        n = int(input('Введите кол/во строк квадратной матрицы: '))
        break
    except ValueError:
        print('Некорректные данные')

new_matrix = [[random.randint(-5, 30) for j in range(n)] for i in range(n)]

for i in new_matrix:
    print(i)

request = False

for i in new_matrix:
    for j in i:
        if j > 0:
            request = True
            break
    if request:
        break

print(request)

