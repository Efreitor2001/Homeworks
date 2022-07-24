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
#     print('🎉| First player wins! Gratz!!! |🙌')
# else:
#     print('🎉| Second player wins! Gratz!!! |🙌')

# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""
