'''Дано два числа.
Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.'''

# Обработка исключений:
#######################################################################
Number_first = input('Введите первое число: ')

while type(Number_first) != float:
    try:
        Number_first = float(Number_first)
    except ValueError:
        print('Неправильный тип данных, введите число')
        Number_first = input('Попробуйте еще раз: ')
#######################################################################
Number_second = input('Введите второе число: ')

while type(Number_second) != float:
    try:
        Number_second = float(Number_second)
    except ValueError:
        print('Неправильный тип данных, введите число')
        Number_second = input('Попробуйте еще раз: ')
#######################################################################
# Конец обработки исключений!!!

summ = Number_first + Number_second
if summ % 5 == 0:
    summ += 1
else:
    summ -= 2

print('Результат:', int(summ))
