'''Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).'''

n = int(input('Введите n: '))

sum_of_factorials = 1   # сумма факториала
curr_factorial = 1  # Текущий факториал

for i in range(2, n + 1):
    curr_factorial *= i
    sum_of_factorials += curr_factorial

print(f'Сумма факториалов равна {sum_of_factorials}.')