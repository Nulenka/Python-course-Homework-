print("Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии. A = 3; B = 5 -> 243 (3⁵); A = 2; B = 3 -> 8")

a = int(input("Enter A number: "))
b = int(input("Enter B number: "))

def power(a, b):
    if b == 1:
        return(a)
    else:
        return(a ** b)
print(power(a, b))

print("Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы. 2 2; 4")

a = int(input("Enter A number: "))
b = int(input("Enter B number: "))
 
def sum(a, b):
    if b == 0:
        return (a)
    else:
        return sum(a + 1, b - 1)
print(sum(a, b))