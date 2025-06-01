from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Создание главного окна GUI############################################################################################
root = Tk()
root.title('Обработка формы')
root.geometry('670x763+445+20')
########################################################################################################################
# Заголовок
title_label = Label(root, text='Форма регистрации пользователя', font=('Arial', 19, 'bold'))
title_label.grid(pady=30, padx=100)
########################################################################################################################

out_wrapper = Frame(root, bg='gray')        # Используется для создания серой рамки
out_wrapper.grid(padx=30)

# Серая граница создается путем накладывания двух фреймов поверх друг друга (Серый + белый)

frame_wrapper = Frame(out_wrapper, bd=2)    # Используется для наложения поверх серого
frame_wrapper.grid(padx=2, pady=2, sticky='ew')     # Внешние отступы дают эффект серой рамки

frame_wrapper.grid_columnconfigure(1, weight=1, minsize=40)
########################################################################################################################
form_label1 = Label(frame_wrapper, text='Ваше имя:', font=('Arial', 17))
form_label1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# ФОРМА ИМЕНИ

form_inter1 = Entry(frame_wrapper, font=('Arial', 17), width=25, bg='#d5d5d5')
form_inter1.grid(row=0, column=2, padx=10, pady=10, sticky='e')
########################################################################################################################
form_label2 = Label(frame_wrapper, text='Пароль:', font=('Arial', 17))
form_label2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

# ФОРМА ПАРОЛЯ

form_inter2 = Entry(frame_wrapper, font=('Arial', 17), width=25, bg='#d5d5d5', show='*')
form_inter2.grid(row=1, column=2, padx=10, pady=10, sticky='e')
########################################################################################################################
form_label3 = Label(frame_wrapper, text='Возраст:', font=('Arial', 17))
form_label3.grid(row=2, column=0, padx=10, pady=10, sticky='w')

# ФОРМА ВОЗРАСТА

form_inter3 = Entry(frame_wrapper, font=('Arial', 17), width=25, bg='#d5d5d5')
form_inter3.grid(row=2, column=2, padx=10, pady=10, sticky='e')
########################################################################################################################
form_label4 = Label(frame_wrapper, text='Пол:', font=('Arial', 17))
form_label4.grid(row=3, column=0, padx=10, pady=10, sticky='w')

gender_var = StringVar(value="Мужской")     # Значение по умолчанию

gender_frame = Frame(frame_wrapper)         # Отдельный фрейм (контейнер) для радио кнопок
gender_frame.grid(row=3, column=2, padx=10, pady=10, sticky='ew')

# ФОРМА ПОЛА

# Растягивание колонок
gender_frame.grid_columnconfigure(0, weight=1)
gender_frame.grid_columnconfigure(1, weight=1)

male_radio = Radiobutton(gender_frame, text='Мужской', variable=gender_var, value='Мужской', font=('Arial', 15))
male_radio.grid(row=0, column=0, sticky='w')

female_radio = Radiobutton(gender_frame, text='Женский', variable=gender_var, value='Женский', font=('Arial', 15))
female_radio.grid(row=0, column=1, sticky='e')
########################################################################################################################
form_label5 = Label(frame_wrapper, text='Ваши увлечения:', font=('Arial', 17))
form_label5.grid(row=4, column=0, padx=10, pady=10, sticky='w')

# Ожидающие параметры
hobby_music = IntVar()
hobby_video = IntVar()
hobby_draw = IntVar()

# ФОРМА УВЛЕЧЕНИЙ

hobby_frame = Frame(frame_wrapper)      # Отдельный фрейм (контейнер) для чек-боксов
hobby_frame.grid(row=4, column=2, padx=10, pady=10, sticky='ew')

# Растягивание колонок
hobby_frame.grid_columnconfigure(0, weight=1)
hobby_frame.grid_columnconfigure(1, weight=1)
hobby_frame.grid_columnconfigure(2, weight=1)

music_cb = Checkbutton(hobby_frame, text='Музыка', variable=hobby_music, font=('Arial', 15))
music_cb.grid(row=0, column=0, sticky='w')

video_cb = Checkbutton(hobby_frame, text='Видео', variable=hobby_video, font=('Arial', 15))
video_cb.grid(row=0, column=1)

draw_cb = Checkbutton(hobby_frame, text='Рисование', variable=hobby_draw, font=('Arial', 15))
draw_cb.grid(row=0, column=2, sticky='e')
########################################################################################################################
form_label6 = Label(frame_wrapper, text='Ваша страна:', font=('Arial', 17))
form_label6.grid(row=5, column=0, padx=10, pady=10, sticky='w')

country_var = StringVar() # Ожидающая переменная

# ФОРМА СТРАНЫ

# Изменение стиля окна выбора
style = ttk.Style()
style.theme_use('default')
style.configure('Custom.TCombobox',     # Меняем параметры дефолтного (по умолчанию) стиля
                fieldbackground='#d5d5d5',
                background='#d5d5d5',
                bordercolor='#d5d5d5',
                relief='flat')

country_combobox = ttk.Combobox(frame_wrapper, textvariable=country_var,
                               font=('Arial', 17), width=24, state='readonly',
                               style='Custom.TCombobox')
country_combobox['values'] = ['Россия', 'Казахстан', 'Беларусь', 'Украина', 'Другое']
country_combobox.grid(row=5, column=2, padx=10, pady=10, sticky='e')
country_combobox.current(0)     # Значение по умолчанию
########################################################################################################################
form_label7 = Label(frame_wrapper, text='Ваш город:', font=('Arial', 17))
form_label7.grid(row=6, column=0, padx=10, pady=10, sticky='w')

city_var = StringVar()      # Ожидающая переменная

# ФОРМА ГОРОДА

city_combobox = ttk.Combobox(frame_wrapper, textvariable=city_var,
                             font=('Arial', 17), width=24, state='readonly',
                             style='Custom.TCombobox')
city_combobox['values'] = ['Ростов - на Дону', 'Анапа', 'Краснодар', 'Батайск', 'Другой']
city_combobox.grid(row=6, column=2, padx=10, pady=10, sticky='e')
city_combobox.current(0)        # Значение по умолчанию
########################################################################################################################
form_label8 = Label(frame_wrapper, text='Кратко о себе:', font=('Arial', 17))
form_label8.grid(row=7, column=0, padx=10, pady=10, sticky='nw')


# ФОРМА КРАТКО-О-СЕБЕ

about_text = Text(frame_wrapper, font=('Arial', 17), width=25, height=3, bg='#d5d5d5', fg='#555555')
about_text.grid(row=7, column=2, padx=10, pady=10, sticky='e')

# Вставляем плейсхолдер
placeholder = 'Краткая информация о ваших увлечениях'
about_text.insert('1.0', placeholder)

# Удаляет плейсхолдер при нажатии на поле
def on_focus_in(event):
    if about_text.get('1.0', 'end-1c') == placeholder:
        about_text.delete('1.0', 'end')
        about_text.config(fg='black')   # Меняет цвет вводимого шрифта на чёрный

# Возвращает плейсхолдер при выходе из поля
def on_focus_out(event):
    if not about_text.get('1.0', 'end-1c').strip():
        about_text.insert('1.0', placeholder)
        about_text.config(fg='#555555')     # Возвращает цвет плейсхолдеру

# Вызов функций при активном ивенте
about_text.bind('<FocusIn>', on_focus_in)
about_text.bind('<FocusOut>', on_focus_out)
########################################################################################################################
form_label9 = Label(frame_wrapper, text='Решите пример, запишите результат в поле ниже:', font=('Arial', 17))
form_label9.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky='w')

# ФОРМА РЕШИТЕ-ПРИМЕР

form_inter9 = Entry(frame_wrapper, font=('Arial', 17), width=25, bg='#d5d5d5')
form_inter9.grid(row=9, column=2, padx=10, pady=10, sticky='e')
########################################################################################################################
# Фрейм (контейнер) для кнопок
buttons_frame = Frame(frame_wrapper)
buttons_frame.grid(row=10, column=2, padx=10, pady=10, sticky='ew')

# Настраиваем колонки
buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)

btn_font = ('Arial', 13)  # Размер шрифта

# Функционал для кнопки очистки данных из формы (Отмена)
def clear_form():
    # Очистка Entry-полей
    form_inter1.delete(0, END)
    form_inter2.delete(0, END)
    form_inter3.delete(0, END)
    form_inter9.delete(0, END)

    # Сброс радио-кнопок
    gender_var.set('Мужской')

    # Сброс чекбоксов
    hobby_music.set(0)
    hobby_video.set(0)
    hobby_draw.set(0)

    # Сброс кнопок выбора
    country_combobox.current(0)
    city_combobox.current(0)

    # Сброс поля Text с плейсхолдером
    about_text.delete('1.0', END)
    about_text.insert('1.0', placeholder)
    about_text.config(fg='#555555')

# Функционал для предупреждения о необходимости заполнения всех полей формы
def error_form():
    warn = messagebox.showwarning('Предупреждение', 'Заполните все поля!')
    clear_form()

# Функционал для кнопки отправки формы
def submit_form():
    # Получение данных с полей
    name = form_inter1.get()
    password = form_inter2.get()
    age = form_inter3.get()
    gender = gender_var.get()

    hobbies = []
    if hobby_music.get():
        hobbies.append('Музыка')
    if hobby_video.get():
        hobbies.append('Видео')
    if hobby_draw.get():
        hobbies.append('Рисование')

    country = country_var.get()
    city = city_var.get()
    about = about_text.get('1.0', END).strip()
    answer = form_inter9.get()

    if all([name, password, age, hobbies, about, answer]):  # Отправка полученных данных
        print("Имя:", name)
        print("Пароль:", password)
        print("Возраст:", age)
        print("Пол:", gender)
        print("Увлечения:", ', '.join(hobbies))
        print("Страна:", country)
        print("Город:", city)
        print("О себе:", about)
        print("Решение примера:", answer)
    else:                                                   # Вызов предупреждения если все поля не заполнены
        error_form()

# Привязка функционала к кнопкам и размещение в фрейме (контейнере)
btn1 = Button(buttons_frame, text='Отмена', font=btn_font, bg='#d5d5d5', width=12, command=clear_form)
btn1.grid(row=0, column=0, sticky='w')

btn2 = Button(buttons_frame, text='Подтвердить', font=btn_font, bg='#d5d5d5', width=12, command=submit_form)
btn2.grid(row=0, column=1, sticky='e')
########################################################################################################################


root.mainloop()     # Главный цикл работы GUI