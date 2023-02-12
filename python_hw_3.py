# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# n = 5; 1 2 3 4 5; x = 3; -> 1

n = int(input("Enter N number: "))
print(f'n = {n}')
A = list(range(1, n + 1))
x = 3
count = 0
for i in range(n):
    if i == x:
        count += 1
print(A)
print(f'x = {x}')
print(f'-> {count} ')
print(" ")

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданномучислу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# n = 5; 1 2 3 4 5; x = 6; -> 5

n = int(input("Enter N number: "))
A = list(range(1, n + 1))
x = int(input("Enter X number: "))
print(f'n = {n}')
result = 0
for i in range(n + 1):
    if abs(i - x) < abs(result - x):
        result = i
print(A)
print(f'x = {x}')
print(f'-> {result} ')
print(" ")

# Задача 20: B настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# B случае c английским алфавитом очки распределяются так: 
# A, E, I, O, U, L, N, S, T, R - 1 очко; D, G - 2 очка; B, C, M, P - 3 очка; F, H, V, W, Y - 4 очка;
# K - 5 очков; J, X - 8 очков; Q, Z - 10 очков. 
# A русские буквы оцениваются так: A, B, E, И, H, O, P, C, T - 1 очко; Д, K, Л, M, П, Y - 2 очка; 
# Б, Г, Ё, b, Я - 3 очка; Й, Ы - 4 очка; Ж, 3, X, Ц, Ч - 5 очков; Ш, Э, Ю - 8 очков; Ф, Щ, Ъ = 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы. Ввод: ноутбук. Вывод: 12.

points = {1:'AEIOULNSTRАВЕИНОРСТ', 2:'DGДКЛМПУ', 3:'BCMPБГЁЬЯ', 4:'FHVWYЙЫ', 5:'KЖЗХЦЧ', 8:'JZШЭЮ', 10:'QZФЩЪ'}
text = input("Enter the word: ").upper()
print(sum([k for i in text for k, v in points.items() if i in v]))
print(" ")

print("Thanks for checking! Have a nice day!")