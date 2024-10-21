'''Ввести двухзначное число.
Если сумма цифр числа четная, то увеличить число на 2,
в противном случае уменьшить на 2.'''

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

if Number_first // 10 + Number_first % 10 % 2 == 0:
    Number_first += 2
else:
    Number_first -= 2

print(int(Number_first))