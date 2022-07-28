from curses.ascii import isdigit
import random
# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# r = random.randint(1, 2)
# candy = 100
# pn = 0
# p1 = 0
# p2 = 0
# print(f"According to the results of the draw, the {r} player goes!")
# while candy > 0:
#     if r == 1:
#         print(f"{candy} candies left")
#         p1 = int(input("The first player goes! Take candies: "))
#         while p1 > candy:
#             p1 = int(input("Error! You can't take more candy than you have left: "))
#         while int(p1) <= 0 or int(p1) > 28:
#             p1 = int(
#                 input("Error!!! You can not take less than 1 and more than 28 candies: "))
#             while p1 > candy:
#                 p1 = int(
#                     input("Error! You can't take more candy than you have left: "))
#         candy -= p1
#         pn = 1
#         print(f"{candy} candies left")
#         if candy == 0:
#             break
#         p2 = int(input("The second player goes! Take candies: "))
#         while p2 > candy:
#             p2 = int(input("Error! You can't take more candy than you have left: "))
#         while int(p2) <= 0 or int(p2) > 28:
#             p2 = int(
#                 input("Error!!! You can not take less than 1 and more than 28 candies: "))
#             while p2 > candy:
#                 p2 = int(
#                     input("Error! You can't take more candy than you have left: "))
#         candy -= p2
#         pn = 2
#         if candy == 0:
#             break
#     else:
#         print(f"{candy} candies left")
#         p2 = int(input("The second player goes! Take candies: "))
#         while p2 > candy:
#             p2 = int(input("Error! You can't take more candy than you have left."))
#         while int(p2) <= 0 or int(p2) > 28:
#             p2 = int(
#                 input("Error!!! You can not take less than 1 and more than 28 candies: "))
#             while p2 > candy:
#                 p2 = int(
#                     input("Error! You can't take more candy than you have left."))
#         candy -= p2
#         pn = 2
#         if candy == 0:
#             break
#         print(f"{candy} candies left")
#         p1 = int(input("The first player goes! Take candies: "))
#         while p1 > candy:
#             p1 = int(input("Error! You can't take more candy than you have left."))
#         while int(p1) <= 0 or int(p1) > 28:
#             p1 = int(
#                 input("Error!!! You can not take less than 1 and more than 28 candies: "))
#             while p1 > candy:
#                 p1 = int(
#                     input("Error! You can't take more candy than you have left."))
#         candy -= p1
#         pn = 1
#         if candy == 0:
#             break
# if pn == 1:
#     print('\n  ------------------------------- ')
#     print('🎉| First player wins! Gratz!!! |🙌')
#     print('  ------------------------------- \n')
# else:
#     print('\n  -------------------------------- ')
#     print('🎉| Second player wins! Gratz!!! |🙌')
#     print('  -------------------------------- \n')

# a) Добавьте игру против бота
# r = random.randint(1, 2)
# candy = 100
# pn = 0
# p1 = 0
# p2 = 0
# print(f"According to the results of the draw, the {r} player goes!")
# while candy > 0:
#     if r == 1:
#         print(f"\n{candy} candies left\n")
#         p1 = int(input("The first player goes! Take candies: "))
#         while p1 > candy:
#             p1 = int(input("Error! You can't take more candy than you have left: "))
#         while int(p1) <= 0 or int(p1) > 28:
#             p1 = int(
#                 input("Error!!! You can not take less than 1 and more than 28 candies: "))
#             while p1 > candy:
#                 p1 = int(
#                     input("Error! You can't take more candy than you have left: "))
#         candy -= p1
#         pn = 1
#         print(f"\n{candy} candies left\n")
#         if candy == 0:
#             break
#         p2 = random.randint(1, 28)
#         while p2 > candy:
#             p2 = random.randint(1, 28)
#         while int(p2) <= 0 or int(p2) > 28:
#             p2 = random.randint(1, 28)
#             while p2 > candy:
#                 p2 = random.randint(1, 28)
#         print(f"Second player take {p2} candies")
#         candy -= p2
#         pn = 2
#         if candy == 0:
#             break
#     else:
#         print(f"\n{candy} candies left\n")
#         p2 = random.randint(1, 28)
#         while p2 > candy:
#             p2 = random.randint(1, 28)
#         while int(p2) <= 0 or int(p2) > 28:
#             p2 = random.randint(1, 28)
#             while p2 > candy:
#                 p2 = random.randint(1, 28)
#         print(f"Second player take {p2} candies")
#         candy -= p2
#         pn = 2
#         if candy == 0:
#             break
#         print(f"\n{candy} candies left\n")
#         p1 = int(input("The first player goes! Take candies: "))
#         while p1 > candy:
#             p1 = int(input("Error! You can't take more candy than you have left."))
#         while int(p1) <= 0 or int(p1) > 28:
#             p1 = int(
#                 input("Error!!! You can not take less than 1 and more than 28 candies: "))
#             while p1 > candy:
#                 p1 = int(
#                     input("Error! You can't take more candy than you have left: "))
#         candy -= p1
#         pn = 1
#         if candy == 0:
#             break
# if pn == 1:
#     print('\n  ------------------------------- ')
#     print('🎉| First player wins! Gratz!!! |🙌')
#     print('  ------------------------------- \n')
# else:
#     print('\n  -------------------------------- ')
#     print('🎉| Second player wins! Gratz!!! |🙌')
#     print('  -------------------------------- \n')

# b) (доп) Подумайте как наделить бота ""интеллектом""
# r = random.randint(1, 2)
# candy = 101
# pn = 0
# p1 = 0
# p2 = random.randint(1, 28)
# print(f"According to the results of the draw, the {r} player goes!")
# while candy > 0:
#     if r == 1:
#         print(f"\n{candy} candies left\n")
#         p1 = int(input("The first player goes! Take candies: "))
#         while p1 > candy:
#             p1 = int(input("Error! You can't take more candy than you have left: "))
#         while int(p1) <= 0 or int(p1) > 28:
#             p1 = int(
#                 input("Error!!! You can not take less than 1 and more than 28 candies: "))
#             while p1 > candy:
#                 p1 = int(
#                     input("Error! You can't take more candy than you have left: "))
#         candy -= p1
#         pn = 1
#         print(f"\n{candy} candies left\n")
#         if candy == 0:
#             break
#         if candy % 29 != 0:
#             while (candy-p2) % 29 != 0:
#                 p2 = random.randint(1, 28)
#             while p2 > candy and (candy-p2) % 29 != 0:
#                 p2 = random.randint(1, 28)
#             while int(p2) <= 0 and (candy-p2) % 29 != 0 or int(p2) > 28 and (candy-p2) % 29 != 0:
#                 p2 = random.randint(1, 28)
#                 while p2 > candy and (candy-p2) % 29 != 0:
#                     p2 = random.randint(1, 28)
#         else:
#             p2 = random.randint(1, 28)
#         print(f"Second player take {p2} candies")
#         candy -= p2
#         pn = 2
#         if candy == 0:
#             break
#     else:
#         print(f"\n{candy} candies left\n")
#         while (candy-p2) % 29 != 0:
#             p2 = random.randint(1, 28)
#         while p2 > candy and (candy-p2) % 29 != 0:
#             p2 = random.randint(1, 28)
#         while int(p2) <= 0 and (candy-p2) % 29 != 0 or int(p2) > 28 and (candy-p2) % 29 != 0:
#             p2 = random.randint(1, 28)
#             while p2 > candy and (candy-p2) % 29 != 0:
#                 p2 = random.randint(1, 28)
#         print(f"Second player take {p2} candies")
#         candy -= p2
#         pn = 2
#         if candy == 0:
#             break
#         print(f"\n{candy} candies left\n")
#         p1 = int(input("The first player goes! Take candies: "))
#         while p1 > candy:
#             p1 = int(input("Error! You can't take more candy than you have left."))
#         while int(p1) <= 0 or int(p1) > 28:
#             p1 = int(
#                 input("Error!!! You can not take less than 1 and more than 28 candies: "))
#             while p1 > candy:
#                 p1 = int(
#                     input("Error! You can't take more candy than you have left: "))
#         candy -= p1
#         pn = 1
#         if candy == 0:
#             break
# if pn == 1:
#     print('\n  ------------------------------- ')
#     print('🎉| First player wins! Gratz!!! |🙌')
#     print('  ------------------------------- \n')
# else:
#     print('\n  -------------------------------- ')
#     print('🎉| Second player wins! Gratz!!! |🙌')
#     print('  -------------------------------- \n')

# # 2. Создайте программу для игры в ""Крестики-нолики"".


# def PrintList(b):
#     for i in range(0, len(b)):
#         for j in range(0, len(b[i])):
#             print(b[i][j], end=' ')
#         print()


# def CheckWins(b):
#     if (b[0][0] == 'X' and b[0][1] == 'X' and b[0][2] == 'X' or b[0][0] == '0' and b[0][1] == '0' and b[0][2] == '0' or
#     b[1][0] == 'X' and b[1][1] == 'X' and b[1][2] == 'X' or b[1][0] == '0' and b[1][1] == '0' and b[1][2] == '0' or
#     b[2][0] == 'X' and b[2][1] == 'X' and b[2][2] == 'X' or b[2][0] == '0' and b[2][1] == '0' and b[2][2] == '0' or
#     b[0][0] == 'X' and b[1][0] == 'X' and b[2][0] == 'X' or b[0][0] == '0' and b[1][0] == '0' and b[2][0] == '0' or
#     b[0][1] == 'X' and b[1][1] == 'X' and b[2][1] == 'X' or b[0][1] == '0' and b[1][1] == '0' and b[2][1] == '0' or
#     b[0][2] == 'X' and b[1][2] == 'X' and b[2][2] == 'X' or b[0][2] == '0' and b[1][2] == '0' and b[2][2] == '0' or
#     b[0][0] == 'X' and b[1][1] == 'X' and b[2][2] == 'X' or b[0][0] == '0' and b[1][1] == '0' and b[2][2] == '0' or
#     b[0][2] == 'X' and b[1][1] == 'X' and b[2][0] == 'X' or b[0][2] == '0' and b[1][1] == '0' and b[2][0] == '0'):
#         return True
#     else:
#         return False


# a = 3
# lst = ['*'] * 3
# p = 0
# i = 0
# j = 0
# step = ''
# for i in range(a):
#     lst[i] = ['*'] * a
# PrintList(lst)
# for g in range(9):
#     if g % 2 == 0:
#         step = "X"
#     else:
#         step = "0"
#     i = int(input()) - 1
#     j = int(input()) - 1
#     while int(i) < 0 or int(i) > 2 or int(j) < 0 or int(j) > 2 or lst[i][j] != '*':
#         print('Error! Specify other coordinates')
#         i = int(input()) - 1
#         j = int(input()) - 1
#     lst[i][j] = step
#     PrintList(lst)
#     CheckWins(lst)
#     if CheckWins(lst) == True:
#         p = step
#         break
# if p == 'X':
#     print("Wins X")
# elif p == '0':
#     print("Wins 0")
# else:
#     print("Friendship won")

# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
import itertools


def compress(text):
    for char, same in itertools.groupby(text):
        count = sum(1 for _ in same)
        yield str(count)+char


def uncompress(rle):
    decode = '' 
    count = '' 
    for i in rle: 
        if i.isdigit():
            count += i 
        else:  
            decode += i * int(count) 
            count = '' 
    return decode 


s = input('Enter: ')
s1 = ''.join(compress(s))
print(s1)
s2 = uncompress(s1)
print(s2)
