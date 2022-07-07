# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
from math import sqrt
day = int(input('Enter the day of the week: '))
while day < 1 or day > 7:
    day = int(input('Error!!! Please enter a valid day: '))
if day == 6 or day == 7:
    print('Is weekend')
else:
    print('Is NOT weekend')

# 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input('Enter X: '))
y = int(input('Enter Y: '))
z = int(input('Enter Z: '))
if not (x or y or z) == (not x) and (not y) and (not z):
    print('True')
else:
    print('False')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
X = float(input('Enter X coordinate: '))
Y = float(input('Enter Y coordinate: '))
while X == 0 or Y == 0:
    print('Error!!! Coordinate must not be 0')
    X = float(input('Enter X coordinate: '))
    Y = float(input('Enter Y coordinate: '))
if X > 0 and Y > 0:
    print('First quarter')
elif X < 0 and Y > 0:
    print('Second quarter')
elif X < 0 and Y < 0:
    print('Third quarter')
else:
    print('Fourth quarter')

# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
qrtr = int(input('Enter quarter: '))
while qrtr < 1 or qrtr > 4:
    qrtr = int(input('Error!!! Enter valid quarter: '))
if qrtr == 1:
    print('X > 0 - (+∞); Y > 0 - (+∞)')
elif qrtr == 2:
    print('X < 0 - (-∞); Y > 0 - (+∞)')
elif qrtr == 3:
    print('X < 0 - (-∞); Y < 0 - (-∞)')
else:
    print(('X > 0 - (+∞); Y < 0 - (-∞)'))

# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
xA = float(input('Enter the X coordinate for point A: '))
yA = float(input('Enter the Y coordinate for point A: '))
xB = float(input('Enter the X coordinate for point B: '))
yB = float(input('Enter the Y coordinate for point B: '))
result = sqrt(((xB-xA)**2 + (yB-yA)**2))
print(round(result, 3))
