'''Ввести 4 числа. Найти и вывести на экран количество четных чисел.'''

k = 0

for i in range(4):
    while True:
        try:
            if int(input(f'Число {i + 1}: ')) % 2 == 0:
                k += 1
            break
        except ValueError:
            print('Некорректное число!')

print(f'{k} четных числа')