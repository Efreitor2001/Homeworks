# Мимикрия
# transformation = lambda x: x
# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# Самая далёкая планета

# def find_farthest_orbit(tpl):
#     p = 3.14
#     lst = []
#     result = ()
#     for i in tpl:
#         a, b = i
#         if a != b:
#             lst.append(a)
#             lst.append(b)
#     s = [p * lst[i] * lst[i + 1] for i in range(0, len(lst), 2)]  # использовал списочное выражение =)
#     max_s = s[0]
#     for i in s:
#         if i > max_s:
#             max_s = i
#     for i in range(0, len(lst), 2):
#         if p * lst[i] * lst[i + 1] == max_s:
#             result = lst[i], lst[i + 1]
#     return result
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Пам-парам парам-пам парам
# def param(s):
#     a = s.split()
#     count = 0
#     cl = []
#     check = 'ауоыэяюёиеaeiouy'
#     for i in a:
#         for j in i:
#             for g in check:
#                 if g in j:
#                     count += 1
#         if count > 0:
#             cl.append(count)
#         count = 0
#     y = cl[0]
#     b = list(filter(lambda x: x == y, cl))  # использовал lamda-функцию в сочетании с функцией высшего порядка =)
#     if len(cl) == len(b):
#         return True
#     else:
#         return False
#
#
# verse = str(input('Enter Your verse: '))
# if param(verse):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

# Все равны, как на подбор
# def same_by(characteristic, objects):
#     a = []
#     for i in objects:
#         if characteristic(i) == 0:
#             a.append(True)
#         else:
#             a.append(False)
#     y = a[0]
#     b = list(filter(lambda x: x == y, a))
#     if len(a) == len(b):
#         return True
#     else:
#         return False
#
#
# values = [0, 2, 4, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
