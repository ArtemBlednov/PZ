'''В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
раза.'''

import random

while True:
    try:
        n = int(input('Введите кол/во строк квадратной матрицы: '))
        break
    except ValueError:
        print('Некорректные данные')

new_matrix = [[random.randint(0, 10) for j in range(n)] for i in range(n)]

print('Первоначальная матрицы:')

for i in new_matrix:
    print(i)

print('Производная матрица:')

for i in range(n):
    for j in range(n):

        if i < j:
            new_matrix[i][j] *= 2
        elif i > j:
            new_matrix[i][j] *= 2



for i in new_matrix:
    print(i)