'''Книжные магазины предлагают следующие коллекции книг.
Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
БукМаркет – Пушкин, Достоевский, Маяковский.
Галерея – Чехов, Тютчев, Пушкин. Определить в каких магазинах
можно приобрести книги Маяковского'''

Magister = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
HomeBook = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
BookMarket = {'Пушкин', 'Достоевский', 'Маяковский'}
Gallery = {'Чехов', 'Тютчев', 'Пушкин'}

store = [Magister, HomeBook, BookMarket, Gallery]
name_store = ['Magister', 'HomeBook', 'BookMarket', 'Gallery']

have = []   # Список магазинов, где доступны книги Маяковского.

for i in range(len(store)):     # Итерация по элементам списка store.
    if 'Маяковский' in store[i]:
        have.append(name_store[i])  # В список have добавляется название магазина, где есть Маяковский.


print(f'Кинги Маяковского присутствуют в магазинах: {" ".join(have)}')