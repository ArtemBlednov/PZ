'''Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в
функции.'''

def geometry(length, width):

    perimeter = 2 * (length + width) # Расчет периметра
    square = length * width # Расчет площади

    return perimeter, square

# Обработка исключений:
while True:
    try:
        length = int(input('Введите длину: '))
        break
    except ValueError:
        print('Ошибка: Введите корректное число.')

#############################################################

while True:
    try:
        width = int(input('Введите ширину: '))
        break
    except ValueError:
        print('Ошибка: Введите корректное число.')

# Конец обработки исключений

result = geometry(length, width) # Результат выполнения функции, данные в виде кортежа
perimeter = result[0] # Присваивание переменой perimeter значения с индексом кортежа 0
square = result[1] # Присваивание переменной square значения с индексом кортежа 1

print(f'Периметр прямоугольника равен {perimeter} см.')
print(f'Площадь прямоугольника равна {square} см.')

