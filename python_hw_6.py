print('Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.')

a1 = int(input("Enter a1: "))
d = int(input("Enter d: "))
n = int(input("Enter n: ")) 

progression = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*progression)
# print(" ")

print("Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)")

from random import randint

hiInd = int(input("Enter the hight index: "))
loInd = int(input("Enter the low index: "))
elements = [randint(1, 10) for _ in range(20)]
print("Start array: ", elements, sep='\n')

indexes = [i for i, v in enumerate(elements) if loInd <= v <= hiInd]
print("Indexes: ", indexes, sep='\n')
