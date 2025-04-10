"""Составить генератор (yield), который выводит из строки только буквы."""

import string

def gen(line):
    yield from [i for i in line if i in string.ascii_letters + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']

line_test = 'Строка с пробелами 124 14 1 23 и цифрами :)) ?:;(?"(;?!'

result = gen(line_test)

print(' '.join(result))