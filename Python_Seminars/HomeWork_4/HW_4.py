from asyncore import write
import random
# 1. Вычислить число c заданной точностью d
# def Pi(n):
#     i = 1
#     x = 3
#     g = 1
#     p = 12**0.5
#     s = ''
#     while i < 10000:
#         if i % 2 != 0:
#             g = g - (1/(x*(3**i)))
#         else:
#             g = g + (1/(x*(3**i)))
#         x += 2
#         i += 1
#     p *= g
#     p = str(p)
#     for i in range(n+2):
#         s += str(p[i])
#     return float(s)


# d = int(input("Enter Your number: "))
# while d < 1 or d > 15:
#     d = int(input("Error! Please Enter a number greater than 0 and less than 16: "))
# print(Pi(d))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых делителей
# числа N. (1 - составное число)
# def Dividers(n):
#     a = []
#     i = 2
#     while i <= n:
#         if n % i == 0:
#             c = 0
#             j = 2
#             while j < i:
#                 if i % j == 0:
#                     c += 1
#                 j += 1
#             if c == 0:
#                 a.append(i)
#         i += 1
#     return a


# n = int(input("Enter Your number: "))
# print(Dividers(n))

# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# def Unique(n):
#     x = 0
#     a = list(n.split())
#     b = []
#     i = 0
#     while i < len(a):
#         x = a[i]
#         c = 0
#         for j in range(len(a)):
#             if int(a[j]) == int(x):
#                 c += 1
#         if c < 2:
#             b.append(int(x))
#         i += 1
#     return b


# num = input('Enter Your numbers separated by a space: ')
# print(f'Unique elements are: {Unique(num)}')

# 4. Задана натуральная степень k.Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.
# def Polynomial(k):
#     s = ''
#     r = 0
#     for i in range(k, 0, -1):
#         r = random.randint(0, 100)
#         if r == 0:
#             s += ''
#         elif r == 1:
#             s += str(f'x^{i} + ')
#         elif i != 1:
#             s += str(f'{r}x^{i} + ')
#         else:
#             s += str(f'{r}x ')
#     r = random.randint(0, 100)
#     if r != 0:
#         s += str(f'+ {r} = 0')
#     else:
#         s += str(f'= 0')
#     return s


# k = int(input("Enter Your power: "))
# while k <= 0:
#     k = int(input("Error! Please enter a power greater than 0: "))
# print(Polynomial(k))

# 5(Доп). Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
with open('/home/efreitor2001/Homeworks/Python_Seminars/HomeWork_4/1.txt') as f1, open('/home/efreitor2001/Homeworks/Python_Seminars/HomeWork_4/2.txt') as f2, open('/home/efreitor2001/Homeworks/Python_Seminars/HomeWork_4/result.txt', 'w') as fr:
    a = list(f1.read().replace('+', ' ').replace('=0', ' ').split())
    b = list(f2.read().replace('+', ' ').replace('=0', ' ').split())
    c = []
    s = ''
    s1 = []
    s2 = []
    ct = 0
    for i in a:
        if 'x' in i or '^' in i:
            s1.append(i.replace('x', '').replace('^', " ").split())
    s1.append(a[-1].split())
    for j in b:
        if 'x' in j or '^' in j:
            s2.append(j.replace('x', '').replace('^', " ").split())
    s2.append(b[-1].split())
    print(s1)
    print(s2)
    for i in s1:
        for j in s2:
            if len(i) > 1:
                if i[-1] == j[-1]:
                    c.append([int(i[0]) + int(j[0]), int(i[-1])])
            if len(i) == 1:
                if len(j) == 1 and ct < 1:
                    c.append(int(i[0]) + int(j[0]))
                    ct += 1
    c.append(int(i[0]) + int(j[0]))
    for i in s1:
        for j in s2:
            if len(i) > 1:
                if i[-1] != j[-1]:
                    c.insert(0, [int(i[0]), int(i[-1])])
                    break
            break
        break
    print(c)
    s = []
    for i in range(len(c)-2):
        s.extend(c[i])
    s.append(c[-2])
    s.append(c[-1])
    for i in range(len(s)-1):
        if i % 2 == 0:
            s[i] = str(f"{s[i]}x^")
        else:
            s[i] = str(f"{s[i]}+")
    if 'x^' in str(s[-2]):
        s[-2] = str(s[-2]).replace("x^", "x+")
    s = " ".join(map(str, s)).replace(" ", "")
    s += '=0'
    print(s)
    fr.write(s)
