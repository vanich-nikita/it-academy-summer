"""
 Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

#lst = [1, 1, 2, 3, 6, 7, 88, 88, 88, 88, 1]
lst = [1, 1, 1, 1]

#a = [int(s) for s in input().split()]
ctr = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            ctr += 1
print(ctr)