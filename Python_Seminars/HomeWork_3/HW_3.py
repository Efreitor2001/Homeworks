import math
from operator import le
from queue import Empty
# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# def Sum(list):
#     sum = 0
#     for i in range(len(list)):
#         if i % 2 != 0:
#             sum += list[i]
#     return sum


# a = [1, 5, 7, 10, 11, 25, 231, 3, 6]
# print(f'Sum of elements in odd positions = {Sum(a)}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# def Product(list):
#     j = len(list) - 1
#     size = math.ceil(len(list) / 2)
#     print(list)
#     for i in range(size):
#         print(f'{list[i]} * {list[j]} = {list[i] * list[j]}')
#         j -= 1


# b = [2, 3, 4, 5, 6]
# Product(b)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# def frac(list):
#     for i in range(len(list)):
#         list[i] = int(round(list[i] - int(list[i]), 2) * 100)
#     return list


# def diff(list):
#     max = list[0]
#     min = list[0]
#     for i in range(len(list)):
#         if list[i] != 0:
#             if list[i] > max:
#                 max = list[i]
#             elif list[i] < min:
#                 min = list[i]
#     return (max-min)/100


# c = [1.1, 1.61, 3.1, 5, 10.01]
# print(c)
# print(diff(frac(c)))


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# def bin(n):
#     res = str("")
#     while n != 0:
#         res += str(n % 2)
#         n //= 2
#     return ''.join(reversed(res))


# n = int(input('Enter Your number: '))
# print(bin(n))

# *5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def Negafibonacci(n):
    if n == 1 or n == 2:
        return -1
    else:
        return Negafibonacci(n + 2) - Negafibonacci(n + 1)


number = input("Enter Your number: ")
if int(number) > 0:
    i = int(number) * (-1)
    e = int(number)
else:
    i = int(number)
    e = int(number) * (-1)
j = 0
while i < 0:
    print(Negafibonacci(i) * (-1), end=" ")
    i += 1
print(0, end=" ")
while j < e:
    j += 1
    print(Fibonacci(j), end=" ")
