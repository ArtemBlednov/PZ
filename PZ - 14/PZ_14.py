"""В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
фразу «Министерства образования Ростовской области», посчитать количество
произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
«50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА."""

import re

file = open('hotline.txt', 'r', encoding='utf-8')

prompt = file.read()
file.close()

# print(prompt)

# Изменение горячей линии
pattrn = re.compile(r'«Горячая линия»')

change_text, count = pattrn.subn('«Горячая линия Министерства образования Ростовской области»', prompt)

print('Измененный текст: ')
print(change_text)

print('Количество изменений: ')
print(count)

new_file = open('hotline_modified.txt', 'w', encoding='utf-8')
new_file.write(change_text)
new_file.writelines(f'Кол/во изменений: {str(count)}')
new_file.close()
###################################################################################################################
# Номера на 03, 50
change_text = re.findall(r'\d+-?\d+03\b', prompt)

new_file = open('hotline_modified.txt', 'a', encoding='utf-8')

print(f'Кол/во номеров заканчивающихся на 03: {len(change_text)}')
new_file.writelines('\n' + f'Кол/во номеров заканчивающихся на 03: {len(change_text)}')

change_text = re.findall(r'\d+-?\d+50\b', prompt)

print(f'Кол/во номеров заканчивающихся на 50: {len(change_text)}')
new_file.writelines('\n' + f'Кол/во номеров заканчивающихся на 50: {len(change_text)}')

new_file.close()
######################################################################################################################
# Номера связанные с ЕГЭ/ГИА

change_text = re.findall(r'.*(ЕГЭ|ГИА).*?(\d{2,}-?\d{2,}).*', prompt)

new_file = open('hotline_modified.txt', 'a', encoding='utf-8')

for match in change_text:
    print(f'Номер связанный с ЕГЭ/ГИА: {match[1]}')
    new_file.writelines('\n' + f'Номер связанный с ЕГЭ/ГИА: {match[1]}')

new_file.close()