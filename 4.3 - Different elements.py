"""
Даны два списка чисел. Посчитайте, сколько различных чисел
содержится одновременно как в первом списке, так и во втором.
"""

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [2, 4, 6, 8, 10, 12]

# the usual way to find the symmetric difference (for test)
# print(list(set(l1) ^ set(l2)))

print(list((lambda a, b: a ^ b)(set(l1), set(l2))))
