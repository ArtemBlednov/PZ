'''Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
результата предусмотреть в основной программе. Расчет суммы цифр оформить в
функции.'''

def Summator(numbers):

    return(sum(int(digit) for digit in str(numbers)))

# Обработка исключений:
while True:
    try:
        num_first = int(input('Введите первое число: '))
        break
    except ValueError:
        print('Ошибка: Введите корректное число.')

#############################################################

while True:
    try:
        num_second = int(input('Введите второе число: '))
        break
    except ValueError:
        print('Ошибка: Введите корректное число.')

#############################################################
while True:
    try:
        num_third = int(input('Введите третье число: '))
        break
    except ValueError:
        print('Ошибка: Введите корректное число.')

# Конец обработки исключений


# Обработка чисел функцией Summator
sum_first = Summator(num_first)
sum_second = Summator(num_second)
sum_third = Summator(num_third)

# Нахождение числа с большей суммой его цифр
if sum_first > sum_second and sum_first > sum_third:
    print(f'Число с наибольшей суммой цифр - {num_first}!')
elif sum_second > sum_first and sum_second > sum_third:
    print(f'Число с наибольшей суммой цифр - {num_second}!')
elif sum_third > sum_first and sum_third > sum_second:
    print(f'Число с наибольшей суммой цифр - {num_third}!')
else:
    print('Есть одинаковые числа!')



