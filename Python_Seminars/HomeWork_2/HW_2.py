from dataclasses import replace

# 1. Напишите программу, которая принимает
# на вход вещественное число и показывает сумму его цифр.


def SD(n):
    n = n.replace(',', '')
    n = n.replace('.', '')
    n = int(n)
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


a = input('Enter Your number: ')
print(SD(a))

# 2. Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N. Факториал


def Factorial(num):
    f = 1
    print(f'{num}!=', end='')
    for i in range(1, num):
        f *= num
        print(i, end='*')
        num -= 1
    print(f'{i+1}={f}')


n = int(input('Enter Your number: '))
Factorial(n)

# 3. Задана последовательность натуральных чисел, завершающаяся числом 0.
# Требуется определить значение второго по величине элемента в этой последовательности,
# то есть элемента,который будет наибольшим, если из последовательности удалить наибольший элемент.


def SortNumbers(n):
    n = list(n)
    n.sort()
    return n[-2]


t = 2193, 42, 3, 165, 9, 43, 2, 84, 0
print(SortNumbers(t))

# 4.* Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.
# Требуется определить: через сколько лет вклад составит не менее Y рублей.


def Bank(q, w, e):
    c = 0
    w = w / 100
    while q < e:
        q += q * w
        round(q)
        c += 1
    return c


q = float(input("Enter deposit amount: "))
w = float(input("Enter percentage per annum: "))
e = float(input("Enter desired amount :"))
print(Bank(q, w, e))