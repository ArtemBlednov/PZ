"""Дан первый член A и знаменатель D геометрической прогрессии. Сформировать и
вывести список размера 10, содержащий 10 первых членов данной прогрессии: A,
A* D, A* D2, A*D3, ... ."""

# Обработка исключений
while True:
    try:
        A = int(input('Введите A: '))
        D = int(input('Введите D: '))

        break
    except ValueError:
        print('Неверный формат входных данных!!!')

# Добавление результата прогрессии в список
geometric_progression = [A * D**i for i in range(10)]


print(geometric_progression)
