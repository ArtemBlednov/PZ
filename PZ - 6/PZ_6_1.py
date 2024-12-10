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
