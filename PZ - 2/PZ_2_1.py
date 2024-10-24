'''
Скорость первого автомобиля Vi км/ч, второго — V2 км/ч, расстояние между ними S км.
Определить расстояние между ними через T часов, если автомобили удаляются друг от друга.
Данное расстояние равно сумме начального расстояния и общего пути, проделанного автомобилями;
общий путь = время • суммарная скорость.
'''

# Обработка исключений:
#######################################################################
first_car = input('Скорость первого автомобиля: ')

while type(first_car) != float:
    try:
        first_car = float(first_car)
    except ValueError:
        print('Неправильный тип входящих данных для скорости первого автомобиля.')
        first_car = input('Попробуйте еще раз: ')
#######################################################################
second_car = input('Скорость второго автомобиля: ')

while type(second_car) != float:
    try:
        second_car = float(second_car)
    except ValueError:
        print('Неправильный тип входящих данных для скорости второго автомобиля.')
        second_car = input('Попробуйте еще раз: ')
#######################################################################
S_car = input('Расcтояние между ними: ')

while type(S_car) != float:
    try:
        S_car = float(S_car)
    except ValueError:
        print('Неправильный тип входящих данных для расстояния между автомобилями!')
        S_car = input('Попробуйте еще раз: ')

time_s = input('Время поездки: ')
#######################################################################
while type(time_s) != float:
    try:
        time_s = float(time_s)
    except ValueError:
        print('Неправильный тип входящих данных для времени!')
        time_s = input('Попробуйте еще раз: ')
#######################################################################
# Конец обработки исключений!!!

S_global = time_s * (first_car + second_car)  # Общий путь

Distance = S_car + S_global  # Расстояние между автомобилями за time_s часов

print(int(Distance))    # Округление ответа!!!