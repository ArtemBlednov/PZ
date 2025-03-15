"""Составить генератор (yield), который выводит из строки только буквы."""

import string

def gen(line):
    yield from [i for i in line if i in string.ascii_letters + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']

line_test = 'Строка с пробелами'

result = gen(line_test)

print(list(result))