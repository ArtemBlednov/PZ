import string

file = open('text18-4.txt', 'r', encoding='utf-16')

copy = file.read()
file.close()

print(copy)

letters = string.ascii_letters + "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

str_1 = [i for i in copy if i in letters]

print()
print(len(str_1), 'буквенных символа')

new_file = open('file3.txt', 'w', encoding='utf-16')
new_file.write(copy.lower())
new_file.close()
