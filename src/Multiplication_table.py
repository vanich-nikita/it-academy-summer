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
P(32,10**15) = 13826382602124302.
Найдите P(64,10**16).
"""


def multiplication_table(m, n):
    result = set()
    try:
        if m <= 0 or n <= 0:
            raise ValueError("Input positive number!")
        else:
            # for "little" numbers
            for row in range(1, m + 1):
                value_of_row = (row * y for y in range(1, n + 1))
                for element in value_of_row:
                    result.add(element)
            print(len(result))
    except ValueError:
            print("ValueError input correct data!")
    except TypeError:
            print("TypeError input correct data!")
    return len(result)


# if __name__ == '__main__':
#     multiplication_table(-1, -1)
#     multiplication_table('a', 'b')
#     multiplication_table(1, 1)
#     multiplication_table(3, 4)
#     multiplication_table(64, 64)
#     multiplication_table(12, 345)
#     multiplication_table(64, 10**6)
