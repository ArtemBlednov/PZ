'''Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном
случае увеличить его в 1.5 раза.'''

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

multip = Number_first * Number_second   # Пременная для условия (произведение двух чисел)

if multip < 0:
    multip *= 8
else:
    multip *= 1.5

print('Результат:', multip)


