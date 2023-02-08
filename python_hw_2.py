print('Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. 5 -> 1 0 1 1 0, 2')

n = int(input("Enter a number of coins: "))
count1 = 0
count0 = 0
for i in range(n):
    coinSide = int(input())
    if coinSide > 0:
        count1 += 1
    if coinSide < 1:
        count0 += 1
if count0 < count1:
    print(f'You should turn {count0} coins around')
else:
    print(f'You should turn {count1} coins around.')
print(' ')

print('Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа. 4 4 -> 2 2, 5 6 -> 2 3')

s = int(input("Enter the summ: "))
p = int(input('Enter the product: '))
for x in range(s + p):
    for y in range(s + p):
        if x + y == s and x * y == p:
            print(x, y)
            break
print(' ')

print('Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. 10 -> 1 2 4 8')

n = int(input("Enter N number: "))
a = 1
while a <= n:
    print(a, end = ' ')
    a = a * 2
print(' ')
