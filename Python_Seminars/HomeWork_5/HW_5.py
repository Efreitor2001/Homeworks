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
r = random.randint(1, 2)
candy = 101
pn = 0
p1 = 0
p2 = random.randint(1, 28)
print(f"According to the results of the draw, the {r} player goes!")
while candy > 0:
    if r == 1:
        print(f"\n{candy} candies left\n")
        p1 = int(input("The first player goes! Take candies: "))
        while p1 > candy:
            p1 = int(input("Error! You can't take more candy than you have left: "))
        while int(p1) <= 0 or int(p1) > 28:
            p1 = int(
                input("Error!!! You can not take less than 1 and more than 28 candies: "))
            while p1 > candy:
                p1 = int(
                    input("Error! You can't take more candy than you have left: "))
        candy -= p1
        pn = 1
        print(f"\n{candy} candies left\n")
        if candy == 0:
            break
        if candy % 29 != 0:
            while (candy-p2) % 29 != 0:
                p2 = random.randint(1, 28)
            while p2 > candy and (candy-p2) % 29 != 0:
                p2 = random.randint(1, 28)
            while int(p2) <= 0 and (candy-p2) % 29 != 0 or int(p2) > 28 and (candy-p2) % 29 != 0:
                p2 = random.randint(1, 28)
                while p2 > candy and (candy-p2) % 29 != 0:
                    p2 = random.randint(1, 28)
        else:
            p2 = random.randint(1, 28)
        print(f"Second player take {p2} candies")
        candy -= p2
        pn = 2
        if candy == 0:
            break
    else:
        print(f"\n{candy} candies left\n")
        while (candy-p2) % 29 != 0:
            p2 = random.randint(1, 28)
        while p2 > candy and (candy-p2) % 29 != 0:
            p2 = random.randint(1, 28)
        while int(p2) <= 0 and (candy-p2) % 29 != 0 or int(p2) > 28 and (candy-p2) % 29 != 0:
            p2 = random.randint(1, 28)
            while p2 > candy and (candy-p2) % 29 != 0:
                p2 = random.randint(1, 28)
        print(f"Second player take {p2} candies")
        candy -= p2
        pn = 2
        if candy == 0:
            break
        print(f"\n{candy} candies left\n")
        p1 = int(input("The first player goes! Take candies: "))
        while p1 > candy:
            p1 = int(input("Error! You can't take more candy than you have left."))
        while int(p1) <= 0 or int(p1) > 28:
            p1 = int(
                input("Error!!! You can not take less than 1 and more than 28 candies: "))
            while p1 > candy:
                p1 = int(
                    input("Error! You can't take more candy than you have left: "))
        candy -= p1
        pn = 1
        if candy == 0:
            break
if pn == 1:
    print('\n  ------------------------------- ')
    print('🎉| First player wins! Gratz!!! |🙌')
    print('  ------------------------------- \n')
else:
    print('\n  -------------------------------- ')
    print('🎉| Second player wins! Gratz!!! |🙌')
    print('  -------------------------------- \n')

# # 2. Создайте программу для игры в ""Крестики-нолики"".


# def PintList(b):
#     for i in range(0, len(b)):
#         for j in range(0, len(b[i])):
#             print(b[i][j], end=' ')
#         print()


# a = 3
# lst = ['*'] * 3
# p = 0
# i = 0
# j = 0
# c = 0
# for i in range(a):
#     lst[i] = ['*'] * a
# PintList(lst)
# while c < 9:
#     i = int(input()) - 1
#     j = int(input()) - 1
#     while int(i) < 0 or int(i) > 2 or int(j) < 0 or int(j) > 2 or lst[i][j] != '*':
#         print('Error! Specify other coordinates')
#         i = int(input()) - 1
#         j = int(input()) - 1
#     lst[i][j] = "x"
#     PintList(lst)
#     c += 1
#     i = int(input()) - 1
#     j = int(input()) - 1
#     while int(i) < 0 or int(i) > 2 or int(j) < 0 or int(j) > 2 or lst[i][j] != '*':
#         print('Error! Specify other coordinates')
#         i = int(input()) - 1
#         j = int(input()) - 1
#     lst[i][j] = "0"
#     PintList(lst)
#     c += 1
