tuple1 = (1, 2, 3, 4)
tuple2 = (2, 3, 4, 5)
tuple3 = (3, 4, 5, 6)

set1 = set(tuple1)
set2 = set(tuple2)
set3 = set(tuple3)

common_elements = set1.intersection(set2, set3)

print("Элементы, которые есть во всех кортежах:", common_elements)
#2
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)

unique_elements = []

for element in tuple1:
    if element not in tuple2 and element not in tuple3:
        unique_elements.append(element)

for element in tuple2:
    if element not in tuple1 and element not in tuple3:
        unique_elements.append(element)

for element in tuple3:
    if element not in tuple1 and element not in tuple2:
        unique_elements.append(element)

print("Уникальные элементы для каждого списка:", unique_elements)
#3
import numpy as np

# Заданные кортежи
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (2, 3, 4, 5, 6)
tuple3 = (3, 4, 5, 6, 7)

# Преобразование кортежей в массивы NumPy
array1 = np.array(tuple1)
array2 = np.array(tuple2)
array3 = np.array(tuple3)

# Нахождение элементов, которые есть в каждом кортеже и находятся на той же позиции
intersection_array = np.intersect1d(np.intersect1d(array1, array2), array3)

# Вывод результата
print(intersection_array)