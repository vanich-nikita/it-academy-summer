"""
1.	Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2.	Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3.	Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
4.	Создайте кортеж из одного элемента, чтобы при итерировании по этому
элементу последовательно выводились значения 1, 2, 3. Убедитесь что len()
исходного кортежа возвращает 1.
"""

lst1 = ['a', 'b', 'c']    #1.
tpl1 = tuple(lst1)
print(tpl1)

tpl2 = ('a', 'b', 'c')    #2.
lst2 = list(tpl2)
print(lst2)

a, b, c = 'a', 2, 'python' #3.

tpl3 = ((1, 2, 3), )
print(len(tpl3))
for i in tpl3:
    for n in i:
        print(n, end = ' ')

