"""Дан список размера N. Найти номер его последнего локального максимума
(локальный максимум — это элемент, который больше любого из своих соседей)."""


list_numbers = [1, 3, 7, 1, 2, 6, 3, 2, 1, 8, 7]
n = len(list_numbers)


last_local_max_index = -1  # Последний индекс не рассматривается (от 1 до n -1)

for i in range(1, n - 1):  # Итерируемся по элементам (кроме первого и последнего)
    if list_numbers[i] > list_numbers[i - 1] and list_numbers[i] > list_numbers[i + 1]:
        last_local_max_index = i

print(last_local_max_index)