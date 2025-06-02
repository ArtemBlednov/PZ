'''
Скорость первого автомобиля Vi км/ч, второго — V2 км/ч, расстояние между ними S км.
Определить расстояние между ними через T часов, если автомобили удаляются друг от друга.
Данное расстояние равно сумме начального расстояния и общего пути, проделанного автомобилями;
общий путь = время • суммарная скорость.
'''

# МОДИФИКАЦИЯ С TKINTER

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Расчёт расстояния')
root.geometry('520x500')

# Скорость первого авто#################################################################################################
label1 = Label(root, text='Скорость первого автомобиля: ', font=('Arial', 17))
label1.grid(column=0, row=0, padx=10, pady=10)

input_label1 = Entry(root, font=('Arial', 17), width=10, bg='#d5d5d5')
input_label1.grid(column=1, row=0, padx=10, pady=10)
# Скорость второго авто#################################################################################################
label2 = Label(root, text='Скорость второго автомобиля: ', font=('Arial', 17))
label2.grid(column=0, row=1, padx=10, pady=10)

input_label2 = Entry(root, font=('Arial', 17), width=10, bg='#d5d5d5')
input_label2.grid(column=1, row=1, padx=10, pady=10)
# Расстояние между ними#################################################################################################
label3 = Label(root, text='Расстояние между ними: ', font=('Arial', 17))
label3.grid(column=0, row=2, padx=10, pady=10, sticky=W)

input_label3 = Entry(root, font=('Arial', 17), width=10, bg='#d5d5d5')
input_label3.grid(column=1, row=2, padx=10, pady=10)
# Время поездки#########################################################################################################
label4 = Label(root, text='Время поездки: ', font=('Arial', 17))
label4.grid(column=0, row=3, padx=10, pady=10, sticky=W)

input_label4 = Entry(root, font=('Arial', 17), width=10, bg='#d5d5d5')
input_label4.grid(column=1, row=3, padx=10, pady=10)
########################################################################################################################

answer_frame = None     # Глобальная переменная

# Функция подтверждения отправки данных и последующий расчёт
def apply():
    global answer_frame

    first = input_label1.get()
    second = input_label2.get()
    s = input_label3.get()
    time = input_label4.get()

    if not all([first, second, s, time]):
        messagebox.showwarning('Заполните поля', 'Заполните все поля!')
        return

    try:
        first_car = float(first)
        second_car = float(second)
        S_car = float(s)
        time_s = float(time)

        if all([first_car, second_car, S_car, time_s]):

            # Удаление существующего фрейма
            if answer_frame is not None:
                answer_frame.destroy()
                answer_frame = None

            S_global = time_s * (first_car + second_car)  # Общий путь

            Distance = S_car + S_global  # Расстояние между автомобилями за time_s часов

            # Создание нового фрейма с ответом
            answer_frame = Frame(root, bg='#d5d5d5')
            answer_frame.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

            answer_label = Label(answer_frame,
                                 text=f'Расстояние между ними за {int(time_s)} (ч|м): \n{int(Distance)} (км/ч | м/c)',
                                 font=('Arial', 17), bg='#d5d5d5')
            answer_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

    except ValueError:
        messagebox.showwarning('Не правильный ввод', 'Не правильный тип данных! (Только числа)')

# Функция для очистки заполненных полей
# Удаление фрейма с ответом
def cancel():
    global answer_frame

    input_label1.delete(0, 'end')
    input_label2.delete(0, 'end')
    input_label3.delete(0, 'end')
    input_label4.delete(0, 'end')

    if answer_frame is not None:
        answer_frame.destroy()
        answer_frame = None     # Возвращаем параметр для пустой переменной



# Контейнер для кнопок
btn_frame = Frame(root)
btn_frame.grid(column=0, row=4, columnspan=2)

# Кнопки подтверждения и отмены
button1 = Button(btn_frame, text='отмена', font=('Arial', 13), bg='#d5d5d5', width=12, command=cancel)
button1.grid(column=0, row=0, padx=10, pady=10)

button2 = Button(btn_frame, text='подтвердить', font=('Arial', 13), bg='#d5d5d5', width=12, command=apply)
button2.grid(column=1, row=0, padx=10, pady=10)


root.mainloop()     # Главный цикл работы GUI