import copy

lst = [(x + y) for x in 'ab' for y in 'bcd']  # Используйте генератор, получить: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
print(lst)
print(lst[::2])  # Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
lst2 = [i + "a" for i in "1234"]  # Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
print(lst2)
print(lst2.pop(1))  # Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
print(lst2)
lst3 = copy.copy(lst2)  # Сопируйте список и добавьте в него элемент '2a'
lst3.append("2a")  # так чтобы в исходном списке этого элемента не было.
print(lst3)
print(lst2)
