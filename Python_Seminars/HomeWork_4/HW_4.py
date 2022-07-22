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
def Unique(n):
    x = 0
    a = list(n.split())
    b = []
    i = 0
    while i < len(a):
        x = a[i]
        c = 0
        for j in range(len(a)):
            if int(a[j]) == int(x):
                c += 1
        if c < 2:
            b.append(int(x))
        i += 1
    return b


num = input('Enter Your numbers separated by a space: ')
print(f'Unique elements are: {Unique(num)}')
