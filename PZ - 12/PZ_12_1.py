"""В последовательности на n целых чисел умножить элементы до n-1 на элемент
n."""

import random

while True:
    try:
        n = int(input('Введите последовательность n чисел: '))
        break

    except ValueError:
        print('Неправильный тип данных!!! Введите целое число.')


data = [random.randint(0, 10) for i in range(n)]

print('Список:')
print(data)

print('n - элемент: ')
print(data[-1])

mult = [i * data[-1] if i != data[-1] else i for i in data]

print('Конечный список:')
print(mult)