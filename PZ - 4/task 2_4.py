'''Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).'''

n = input('Введите n: ')

# Обработка исключения
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Вы ввели некорректное число!')
        n = input('Введите n: ')
#############################################

sum_of_factorials = 1   # сумма факториала
curr_factorial = 1  # Текущий факториал

for i in range(2, n + 1):
    curr_factorial *= i
    sum_of_factorials += curr_factorial

print(f'Сумма факториалов равна {sum_of_factorials}.')
