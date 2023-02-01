print('Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3); 100 -> 1 (1 + 0 + 0)')

n = int(input("Enter a 3-digit number, please: "))
if n > 99 and n < 1000 and n % 1 == 0:
    print((n - n % 100) / 100 + (n % 100 - n % 10) / 10 + n % 10)
else:
    print ('Try again, please!')
print(" ")

print('Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе? 6 -> 1 4 1; 24 -> 4 16 4; 60 -> 10 40 10')

s = int(input("Enter a number of paper crains, please: "))
if s >= 4 and s % 6 == 0:
    print (f'Kate made {(s / 6 ) * 4} paper crains.')
    print (f'Peter made {s / 6} paper crains.')
    print (f'Sergey made {s / 6} paper crains.')
else:
    print ('Try again, please!')
print(" ")

print('Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.385916 -> yes; 123456 -> no.')

a = int(input("Enter a 6-digit number, please: "))
if a > 99999 and a < 1000000:
    if ((a - a % 100000) / 100000) + ((a % 100000 - a % 10000) / 10000) + ((a % 10000 - a % 1000) / 1000) == ((a % 1000 - a % 100) / 100) + ((a % 100 - a % 10) / 10) + (a % 10):
        print('Yes, lucky you!')
    else:
        print('Sorry, it is not your day today!')
else:
    print ('Try again, please!')
print(" ")

print('Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 3 2 4 -> yes; 3 2 1 -> no.')

n = int(input("Enter n number, please: "))
m = int(input("Enter m number, please: "))
k = int(input("Enter k number, please: "))
if k < n * m and (k % n == 0 or k % m == 0):
    print("Yes, you can!")
else:
    print("No, sorry!")
print(" ")
