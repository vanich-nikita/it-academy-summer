"""
Пусть P(m,n) будет количеством различных элементов в таблице умножения m×n.
Например, таблица умножения 3×4 выглядит следующим образом:
×	1	2	3	4
1	1	2	3	4
2	2	4	6	8
3	3	6	9	12
В ней 8 различных элементов {1,2,3,4,6,8,9,12}, поэтому P(3,4) = 8.
Известно, что:
P(64,64) = 1263,
P(12,345) = 1998 и
P(32,1015) = 13826382602124302.
Найдите P(64,1016).
"""


def multiplication_table(m, n):
    if m > 0 and n > 0:
        table = {}
        for row in range(1, m + 1):
            table[row] = [row * y for y in range(1, n + 1)]

    result = set()

    for element in table.values():
        result.update(set(element))

    print(len(result))


if __name__ == '__main__':
    multiplication_table(3, 4)
    multiplication_table(64, 64)
    multiplication_table(12, 345)