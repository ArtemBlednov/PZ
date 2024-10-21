'''Вести число. Если оно четное, разделить его на 4,
если нечетное - умножить на 5.'''

# Обработка исключений:
#######################################################################
Number_first = input('Введите число: ')

while type(Number_first) != float:
    try:
        Number_first = float(Number_first)
    except ValueError:
        print('Неправильный тип данных, введите число')
        Number_first = input('Попробуйте еще раз: ')
#######################################################################

if Number_first % 2 == 0:
    Number_first /= 4
else:
    Number_first *= 5

print(int(Number_first))