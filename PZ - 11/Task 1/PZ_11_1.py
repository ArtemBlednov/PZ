
num = ['1', '2', '3', '4', '5', '6', '7', '8', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8']

f = open('file', 'w')
f.writelines(' '.join(num))     # Записываем элементы списка с добавлением пробелов
f.close()


# Читаем строку из file и копируем в переменную
f_read = open('file', 'r')

copy = f_read.readlines()

f_read.close()
#################################################


copy = copy[0].split() # Разбиваем строку списка на множество элементов


# Преобразование списка из элементов строк в числа
int_copy = []


for i in copy:
    int_copy.append(int(i))
#################################################



f2 = open('file2', 'w')
f2.writelines(' '.join(copy))
f2.writelines('\n' + str(len(copy)))

f2.writelines('\n' + str(min(int_copy)))



multiplication = max(int_copy)      # Максимальный элемент на который будем умножать

copy_mult = []  # Список чисел умноженных на multiplication

for i in int_copy:
    copy_mult.append(i * multiplication)






copy_mult = ' '.join(map(str, copy_mult))



f2.writelines('\n' + copy_mult)

f2.close()












