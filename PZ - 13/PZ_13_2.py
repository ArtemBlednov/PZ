'''Если в двумерном списке имеются положительные элементы, то вывести TRUE,
иначе FALSE.'''

import random
from functools import reduce
from tkinter.ttk import Treeview

while True:
    try:
        n = int(input('Введите кол/во строк квадратной матрицы: '))
        break
    except ValueError:
        print('Некорректные данные')

new_matrix = [[random.randint(-5, 30) for j in range(n)] for i in range(n)]

for i in new_matrix:
    print(i)

request = any(any(j > 0 for j in i) for i in new_matrix)

print(request)

