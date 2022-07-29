# Мимикрия
# transformation = lambda x: x
# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# Самая далёкая планета

def find_farthest_orbit(tpl):
    p = 3.14
    lst = []
    result = ()
    for i in tpl:
        a, b = i
        if a != b:
            lst.append(a)
            lst.append(b)
    s = [p * lst[i] * lst[i + 1] for i in range(0, len(lst), 2)]  # использовал списочное выражение =)
    max_s = s[0]
    for i in s:
        if i > max_s:
            max_s = i
    for i in range(0, len(lst), 2):
        if p * lst[i] * lst[i + 1] == max_s:
            result = lst[i], lst[i + 1]
    return result


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
