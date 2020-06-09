"""
Определения:
●  Шоколадка - прямоугольник, размером n×m (n, m - натуральные).
●  Разлом - деление шоколадки на две части с натуральными размерами по прямой.
●  Долька - элемент шоколадки размером 1х1. Очевидно шоколадка состоит из n*m долек.
●  Кусок - элемент шоколадки произвольного (целочисленного размера).
1. Определите, можно ли одним разломом отделить от шоколадки кусок площадью ровно k.
2. Определите, можно ли отломить от шоколадки ровно k долек за некоторое количество разломов.
3. Определите, можно ли отломить от шоколадки ровно k долек с помощью t разломов

1. Отделить от шоколадки кусок площадью k - это значит, что кусок k должен быть с такими сторонами,
что они должны содержать целое число либо сторон n (вертикаль),
либо целое число сторон m (горизонаталь), и, естественно, площадь меньше, чем m*n.

2. Во втором и третьем случаях разломы могут начинать как с горизонтальной стороны,
так и с вертикальной (поэтому в каждом пункте по 2 однотипные переменные).
Количество и возможность разлома основаны на текущей величине сторон,
которая уменьшается с каждым разломом. Смысл проверки тот же: оставшееся число долек
проверяется на целочисленное деление на текущие стороны шоколадки.

3. В третьем случае вводится переменная для посчета разломов,
которая сравнивается с введенным значением.
"""

# 1.
n = int(input("#1. Введите ширину: "))
m = int(input("Введите длину: "))
k = int(input("Введите площаль куска: "))

if ((k % n == 0) or (k % m == 0)) and k < n * m:
    print('Результат: YES')
else:
    print('Результат: NO')

# 2.
# разлом начинается с горизонтали
n1 = int(input("#2. Введите ширину: "))
n2 = n1
m1 = int(input("Введите длину: "))
m2 = m1
k1 = int(input("Введите число долек: "))
k2 = k1

print("Ширина: {}, длина: {}, \
число долек {}".format(n1, m1, k1))
# флаг
flag1 = False
# переменная для подсчета разломов
res1 = k1 // m1
# при отломе от длинной стороны короткая должна уменьшиться
n1 = n1 - res1
# проверка условия
if (k1 % m1) % n1 == 0:
    flag1 = True
    # для проверки выполнения программы
    print('Промежуточный результат: YES1')

# разлом начинается с вертикали
flag2 = False
res2 = k2 // n2
m2 = m2 - res2
if (k2 % n2) % m2 == 0:
    flag2 = True
    print('Промежуточный результат: YES2')

if flag1 or flag2:
    print('Результат: YES')
else:
    print('Результат: NO')

# 3.
# разлом начинается с горизонтали
n3 = int(input("#3. Введите ширину: "))
n4 = n3
m3 = int(input("Введите длину: "))
m4 = m3
k3 = int(input("Введите число долек: "))
k4 = k3
t = int(input("Введите предполагаемое число разломов: "))

print("Ширина: {}, длина: {}, число долек {}, \
число разломов {}".format(n3, m3, k3, t))
# переменная для подсчета разломов
t_res3 = 0
# флаг
flag3 = False
# переменная для подсчета отломанных гориз-ых рядов
res3 = k3 // m3
# при отломе от горизонтальной стороны вертикальная должна уменьшиться
n3 = n3 - res3
# суммарное число разломов для данных входных данных
t_res3 = k3 // m3 + (k3 % m3) // n3
# проверка условия
if (k3 % m3) % n3 == 0 and t == t_res3:
    flag3 = True
    # для проверки выполнения программы
    print('Промежуточный результат: YES3')

# разлом начинается с вертикали
flag4 = False
res4 = k4 // n4
m4 = m4 - res4
t_res4 = k4 // n4 + (k4 % n4) // m4

if (k4 % n4) % m4 == 0 and t == t_res4:
    flag4 = True
    print('Промежуточный результат: YES4')

if flag3 or flag4:
    print('Результат: YES')
else:
    print('Результат: NO')
